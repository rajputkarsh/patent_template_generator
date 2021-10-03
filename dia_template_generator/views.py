from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers.json import DjangoJSONEncoder

# additional imports
import urllib3
from bs4 import BeautifulSoup
from docxtpl import DocxTemplate, RichText
from datetime import datetime     
import json

# translator API
# import translators as ts

import traceback

# base directory
from pathlib import Path
import os
BASE_DIR = Path(__file__).resolve().parent.parent

# helper functions --
def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

def generateRichText(claim_element):

    # replace greater than and lesser than symbols
    claim_element = claim_element.replace("&lt;", "<")
    claim_element = claim_element.replace("&gt;", ">")
    
    # remove div tags if any because they are now meant to be here anymore
    claim_element = " ".join(claim_element.split("<div>"))
    claim_element = " ".join(claim_element.split("</div>"))

    # remove all image tags


    claimElementRichText = RichText()
    
    # check for subscript and superscript tag
    while "<sub>" in claim_element or "<sup>" in claim_element:

        # subscript
        subscript_text = find_between(claim_element, "<sub>", "</sub>")
        if subscript_text != "" and subscript_text != None:
            text = claim_element.split("<sub>"+subscript_text+"</sub>", 1)
            claimElementRichText.add(text[0], subscript=False, bold=False)
            claimElementRichText.add(subscript_text, subscript=True, bold=False)
            claim_element = text[1]

        # superscript
        superscript_text = find_between(claim_element, "<sup>", "</sup>")
        if superscript_text != "" and superscript_text != None:
            text = claim_element.split("<sup>"+superscript_text+"</sup>", 1)
            claimElementRichText.add(text[0], superscript=False, bold=False)
            claimElementRichText.add(superscript_text, superscript=True, bold=False)
            claim_element = text[1]

    claimElementRichText.add(claim_element, subscript=False, bold=False)    


    return claimElementRichText

# view functions

@csrf_exempt
def index(request, *args, **kwargs):
    return HttpResponse("This is the index page")


@csrf_exempt
def generateTemplate(request, *args, **kwargs):

    patentNumber = kwargs['patent_number']
    target_claim_number = 1

    output = {}

    try:
        target_claim_number = int(kwargs['target_claim'])
        if target_claim_number < 1:
            target_claim_number = 1  
    except Exception as e:
        target_claim_number = 1    

    # parsing the patent by web scraping google patents
    URL = "https://www.google.com/patents/"+patentNumber+"/en"
    response = urllib3.PoolManager().request("GET", URL, headers={'User-Agent' : "python"})

    # check if response is successful 
    if int(response.status) == 200:
        
        # parsed html to fetch data
        soup = BeautifulSoup(response.data.decode('utf-8'), 'html.parser')

        try:
            translate = False
            if patentNumber.startswith(('KR', 'CN', 'JP')):    
                translate = True   

            # fetching data for the patent
            title                     = soup.find("title").text.split("-", 1)[1].rsplit("-", 1)[0   ].strip()

            inventors                 = ", ".join([inventor.text for inventor in soup.findAll(itemprop="inventor")])

            filing_date               = soup.find(itemprop="filingDate").text.strip()
            publication_date          = soup.find(itemprop="publicationDate").text.strip()
            priority_date             = soup.find(itemprop="priorityDate").text.strip()

            assignee_original         = soup.find(itemprop="assigneeOriginal").text.strip()
            assignee_current          = soup.find(itemprop="assigneeCurrent").text.strip() if soup.find(itemprop="assigneeCurrent") is not None else ""

            claims                    = soup.find(itemprop="claims" )
            claim_count               = claims.find(itemprop="count").text.strip()
            independent_claims        = [claim.find("div",{"class":"claim"}) for claim in claims.findAll("div",{"class":"claim"}) if claim.find("div",{"class":"claim"})]
            
            
            independent_claim_numbers = ", ".join([ "#"+str(div['num']) for div in independent_claims])

            target_claim_texts        = []
            # try-except condition to avoid errors arising due to patents of different jurisdictions
            try:
                target_claim_texts        = [target_claim_text for target_claim_text in claims.find(num=str(target_claim_number).zfill(5)).findAll("div", {"class" : "claim-text"})]
            except Exception as e:
                target_claim_texts        = [target_claim_text for target_claim_text in claims.find(num=str(target_claim_number)).findAll("div", {"class" : "claim-text"})]
            

            # current date
            today = datetime.today().strftime("%B %d, %Y")


            # generating document from template
            
            doc = DocxTemplate(os.path.join(os.path.join(BASE_DIR, "templates"), "template_dia.docx"))

            context = { 
                'patent_number'             : patentNumber,
                'title'                     : title,
                'inventors'                 : inventors,
                'filing_date'               : filing_date,
                'publication_date'          : publication_date,
                'priority_date'             : priority_date,
                'assignee_original'         : assignee_original,
                'assignee_current'          : assignee_current,
                'claim_count'               : claim_count,
                'independent_claims'        : str(len(independent_claims)),
                'independent_claim_numbers' : independent_claim_numbers,
                'target_claim_number'       : target_claim_number,
                'date'                      : today,
                }

            target_claim_elements = []

            preamble = str(target_claim_texts.pop(0)).split('<div class="claim-text">')[1].replace("<br/>", "\n").strip()
            target_claim_elements.append(preamble)
            modified_claim_text = [{"index" : "0", "claimNumber" : "1", "label" : "Preamble", "claim" : generateRichText(preamble)}]


            #  validating and adding remaining claim elements
            i = 0
            for data in target_claim_texts:
                claim_elements = str(data).split('<div class="claim-text">')
                for claim in claim_elements:
                    if BeautifulSoup(claim, "html.parser").text.strip() != "" and BeautifulSoup(claim, "html.parser").text.strip() != None:
                        if " ".join(claim.split("</div>")).strip() not in target_claim_elements:
                            target_claim_elements.append(" ".join(claim.split("</div>")).strip())
                            modified_claim_text.append({"index" : str(i+1), "claimNumber" : str(i+2), "label" : "Clause "+str(i+1), "claim" : generateRichText(claim.strip()) })        
                            i += 1                
                            

            context['claim_availability_matrix_contents'] = modified_claim_text

            # translate document if required
            # if translate:
            #     print("Translating document")
                
            #     context['title']             = ts.google(context['title'])
            #     context['inventors']         = ts.google(context['inventors'])
            #     context['assignee_original'] = ts.google(context['assignee_original'])

            #     if context['assignee_current'] != "":
            #         context['assignee_current'] = ts.google(context['assignee_current'])

            #     for i in range(len(modified_claim_text)):
            #         modified_claim_text[i]['claim'] =  ts.google(modified_claim_text[i]['claim'])

            document_path = os.path.join(os.path.join(BASE_DIR, "media"), patentNumber+"_DIA.docx")                

            doc.render(context)
            doc.save(document_path)

            output['status']  = 1
            output['message'] = "Template generated"
            output['data'] = "media/{0}_DIA.docx".format(patentNumber)


            # debugging for known errors
            # with open(os.path.join(os.path.join(os.path.join(BASE_DIR, "media"), "html"), patentNumber+".html")  , "w", encoding='utf-8') as file:
            #     file.write(str(soup))

            #debugging ends

        except Exception as error:
            # save parsed html for studying it
            traceback.print_exc()
            
            with open(os.path.join(os.path.join(os.path.join(BASE_DIR, "media"), "html"), patentNumber+".html")  , "w", encoding='utf-8') as file:
                file.write(str(soup))

            output['status']  = 0
            output['message'] = error


    # if response is not successful
    else:
        output['status']  = 0
        output['message'] = "Invalid Patent"

    return HttpResponse(json.dumps(output, cls=DjangoJSONEncoder))