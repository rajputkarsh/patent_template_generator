
import requests

patentsToBeChecked = ['US7932521B2', 'US8128272B2', 'US10230060B2', 'US10593896B2', 'US9609771B2', 'US9722193B2', 'US9997727B2', 'US10593900B2', 'US10340319B2', 'US9183572B2', 'US11056052B2', 'US10196565B2', 'US8883325B2', 'US9099410B2', 'US8852756B2', 'US10502995B2', 'US7748634B1', 'US10467952B2', 'US9743486B2', 'US10103359B2', 'US7776456B2', 'US8035103B2', 'US10620745B2', 'US9493348B2', 'US9076988B2', 'US8232350B2', 'US8995022B1', 'US8993123B2', 'US10025355B2', 'US8328375B2', 'US8780039B2', 'US9300347B1', 'US7619597B2', 'US8889271B2', 'US7820822B2', 'US9929370B2', 'US8284332B2', 'US9024312B2', 'US8476828B2', 'US7633586B2', 'US8901268B2', 'US9331281B2', 'US8315080B2', 'US9233923B2', 'US8247089B2', 'US8471464B2', 'US8027086B2', 'US10615376B2', 'US7978187B2', 'US7973902B2', 'US9818983B2', 'US8493293B2', 'US8610112B2', 'US8885018B2', 'US8253665B2', 'US7940286B2', 'US7714810B2', 'US8351014B2', 'US10322675B2', 'US8786645B2', 'US10088930B2', 'US7948170B2', 'US10613439B2', 'US8648772B2', 'US9120290B2', 'US8573784B2', 'US7807068B2', 'US7923919B2', 'US10082603B2', 'US8170631B2', 'US8314416B2', 'US8956907B2', 'US8581262B2', 'US7868880B2', 'US8368677B2', 'US8733277B2', 'US9343678B2', 'US10103205B2', 'US10036832B2', 'US9100998B2', 'US8044893B2', 'US8558853B2', 'US8547015B2', 'US8358299B2', 'US10020374B2', 'US9502690B2', 'US8188946B2', 'US9905810B2', 'US8764239B2', 'US10403857B2', 'US8742412B2', 'US10381335B2', 'US9847512B2', 'US8334545B2', 'US8044390B2', 'US8889268B2', 'US9112168B2', 'US7973319B2', 'US7990338B2', 'US8723413B2', 'US10339359B2', 'US8823254B2', 'US8183766B2', 'US8026876B2', 'US8986852B2', 'US10572041B2', 'US9720149B2', 'US9933820B2', 'US8796699B2', 'US9182631B2', 'US8564187B2', 'US7965851B2', 'US8404159B2', 'US11020605B2', 'US10535292B2', 'US8593061B2', 'US7736754B2', 'US8860708B2', 'US8848124B2', 'US9287504B2', 'US8248562B2', 'US8410685B2', 'US8766883B2', 'US8159449B2', 'US8148891B2', 'US8670025B2', 'US8921841B2', 'US8363189B2', 'US7910271B2', 'US8212749B2', 'US9444062B2', 'US10243030B2', 'US7521718B2', 'US8646939B2', 'US8685201B2', 'US8110294B2', 'US8952609B2', 'US8956018B2', 'US9095033B2', 'US8461594B2', 'US8380327B2', 'US8796719B2', 'US8241763B2', 'US9183779B2', 'US9013884B2', 'US7956531B2', 'US8858003B2', 'US10782809B2', 'US7629691B2', 'US8574661B2', 'US8854326B2', 'US7852324B2', 'US8614680B2', 'US8569763B2', 'US8420978B2', 'US7649525B2', 'US8436348B2', 'US9091415B2', 'US9449809B2', 'US7738001B2', 'US8877353B2', 'US9379323B2', 'US10361395B2', 'US8743160B2', 'US9052102B2', 'US10483210B2', 'US10005264B2', 'US10503074B2', 'US9384691B2', 'US10288773B2', 'US8729541B2', 'US10032826B2', 'US8764255B2', 'US10049622B2', 'US8970520B2', 'US7816856B2', 'US8274633B2', 'US8469551B2', 'US7815983B2', 'US7615506B2', 'US9786255B2', 'US9385168B2', 'US9711723B2', 'US8115326B2', 'US7989314B2', 'US10775671B2', 'US8537311B2', 'US10147772B2', 'US8791453B2', 'US10388836B2', 'US8058802B2', 'US8994012B2', 'US9512976B2', 'US8299984B2', 'US8697235B2', 'US9767728B2', 'US8599155B2', 'US9221770B2', 'US9958988B2', 'US9984618B2', 'US8823612B2', 'US9103982B2', 'US10809830B2', 'US10719156B2', 'US9299933B2', 'US8476119B2', 'US7868859B2', 'US9082345B2', 'US9385334B2', 'US8742312B2', 'US10834986B2', 'US8830202B2', 'US9529424B2', 'US8915121B2', 'US8063887B2', 'US8405100B2', 'US9252392B2', 'US9224963B2', 'US7872412B2', 'US8062707B2', 'US7851995B2', 'US7952498B2', 'US8054391B2', 'US10520782B2', 'US7586497B2', 'US9899636B2', 'US7982693B2', 'US7724245B2', 'US7969085B2', 'US8513670B2', 'US9142188B2', 'US9058772B2', 'US10217404B2', 'US7440071B2', 'US8680542B2', 'US10116886B2', 'US8456478B2', 'US9854975B2', 'US8563113B2', 'US8827536B2', 'US10234975B2', 'US9236425B2', 'US9961178B2', 'US8569744B2', 'US8890408B2', 'US7781967B2', 'US8084938B2', 'US9674922B2', 'US8310146B2', 'US8987711B2', 'US7474049B2', 'US8901587B2', 'US9944627B2', 'US9373806B2', 'US8154534B2', 'US8421065B2', 'US8723835B2', 'US9171895B2', 'US9720534B2', 'US10043836B2', 'US7623102B2', 'US9925754B2', 'US9887384B2', 'US10069099B2', 'US7837780B2', 'US9120187B2', 'US9312494B2', 'US7951450B2', 'US8053977B2', 'US7948179B2', 'US8580400B2', 'US10879477B2', 'US10804499B2', 'US9231212B2', 'US10409080B2', 'US10789444B2', 'US10332929B2', 'US10481278B2', 'US7495389B2', 'US9093019B2', 'US7922357B2', 'US9334260B2', 'US7741769B2', 'US8582209B1', 'US7821583B2', 'US9660205B2', 'US8816339B2', 'US8227094B2', 'US8884272B2', 'US10191581B2', 'US9817520B2', 'US10691913B2', 'US7541737B2', 'US8436528B2', 'US8587529B2', 'US9465463B2', 'US9117977B2', 'US8183064B2', 'US9102616B2', 'US8822986B2', 'US7838876B2', 'US8628864B2', 'US9955602B2', 'US10050229B2', 'US8933442B2', 'US8243045B2', 'US8785001B2', 'US8558765B2', 'US9305487B2', 'US8692237B2', 'US8674964B2', 'US9530984B2', 'US10763296B2', 'US9692006B2', 'US9755191B2', 'US8569747B2', 'US8111217B2', 'US10405427B2', 'US10381420B2', 'US9736466B2', 'US8902135B2', 'US9978989B2', 'US7850359B2', 'US8692820B2', 'US9860960B2', 'US9196862B2', 'US9159945B2', 'US8587750B2', 'US9929374B2', 'US8686139B2', 'US8749622B2', 'US7615778B2', 'US10100985B2', 'US8136911B2', 'US9887379B2', 'US8085248B2', 'US8933468B2', 'US9196849B2', 'US8698396B2', 'US11011723B2', 'US8778511B2', 'US8276823B2', 'US8669924B2', 'US9774006B2', 'US7710030B2', 'US7459859B2', 'US7812519B2', 'US8823693B2', 'US9099683B2', 'US9482873B2', 'US10339863B2', 'US8018147B2', 'US8094096B2', 'US8466854B2', 'US8754399B2', 'US10916704B2', 'US7902751B2', 'US7800565B2', 'US8791881B2', 'US9647229B2', 'US9324947B2', 'US7800303B2', 'US9312495B2', 'US8241713B2', 'US9099036B2', 'US9977272B2', 'US8866783B2', 'US10229960B2', 'US9812667B2', 'US10795509B2', 'US8599116B2', 'US7964421B2', 'US8766291B2', 'US8487911B2', 'US7576364B2', 'US8008853B2', 'US9679952B2', 'US8319231B2', 'US8914246B2', 'US8772075B2', 'US9761638B2', 'US7876037B2', 'US10553805B2', 'US7719497B2', 'US8497821B2', 'US10036840B2', 'US9337249B2', 'US9207790B2', 'US7649515B2', 'US9508959B2', 'US9530828B2', 'US8203541B2', 'US8129037B2', 'US8822987B2', 'US8520180B2', 'US8455283B2', 'US9871225B2', 'US10289229B2', 'US10503327B2', 'US9075485B2', 'US9537013B2', 'US8294359B2', 'US8016631B2', 'US7935962B2', 'US8829509B2', 'US8610359B2', 'US7656085B2', 'US7800295B2', 'US8513879B2', 'US8330152B2', 'US10983646B2', 'US8871545B2', 'US7566254B2', 'US9134825B2', 'US9437838B2', 'US9262030B2', 'US10185422B2', 'US8436968B2', 'US9276045B2', 'US8063559B2', 'US8323527B2', 'US9082999B2', 'US9141207B2', 'US10228564B2', 'US7449697B2', 'US8040046B2', 'US8217861B2', 'US7722947B2', 'US9644070B2', 'US9627653B2', 'US8633497B2', 'US9471167B2', 'US7642710B2', 'US7683862B2', 'US8546820B2', 'US9117782B2', 'US10204973B2', 'US10461260B2', 'US9600106B2', 'US9859527B2', 'US9082730B2', 'US10854839B2', 'US9866769B2', 'US9812074B2', 'US8044582B2', 'US7782413B2', 'US8487308B2', 'US8263968B2', 'US8199074B2', 'US8247811B2', 'US9207819B2', 'US8803815B2', 'US8492184B2', 'US9041280B2', 'US7550194B2', 'US9735210B2', 'US7667891B2', 'US8158985B2', 'US8568182B2', 'US7659664B2', 'US9117778B2', 'US8749500B2', 'US9478590B2', 'US7888867B2', 'US9831467B2', 'US8237672B2', 'US8264482B2', 'US10446791B2', 'US8436819B2', 'US9214501B2', 'US7642552B2', 'US10198044B2', 'US8269217B2', 'US9941261B2', 'US9378676B2', 'US8022624B2', 'US8796704B2', 'US8592614B2', 'US7923926B2', 'US8687259B2', 'US9368731B2', 'US8482010B2', 'US9047814B2', 'US8624805B2', 'US9105858B2', 'US9673419B2', 'US7923920B2', 'US10325967B2', 'US9007350B2', 'US7868542B2', 'US9093399B2', 'US10483333B2', 'US7800556B2', 'US7915804B2', 'US8310152B2', 'US8237162B2', 'US9058780B2', 'US9345131B2', 'US9128324B2', 'US9508285B2', 'US10394374B2', 'US10579855B2', 'US7436113B2', 'US7928646B2', 'US7977877B2', 'US8242687B2', 'US8502445B2', 'US9853243B2', 'US8003978B2', 'US8253158B2', 'US9391295B2', 'US9171891B2', 'US9466656B2', 'US7893608B2', 'US7812345B2', 'US10104815B2', 'US8841655B2', 'US9324954B2', 'US9879177B2', 'US10651252B2', 'US9983743B2', 'US7538489B2', 'US8222804B2', 'US8624275B2', 'US8710739B2', 'US9660003B2', 'US8610749B2', 'US8482910B2', 'US9489887B2', 'US8502754B2', 'US7795807B2', 'US8158986B2', 'US8994677B2', 'US9230467B2', 'US7915823B2', 'US8729596B2', 'US9547252B2', 'US7872706B2', 'US8466476B2', 'US8860298B2', 'US9118033B2', 'US9379168B2', 'US9130195B2', 'US9711759B2', 'US9252396B2', 'US8247959B2', 'US8159117B2', 'US10185430B2', 'US9520715B2', 'US10008552B2', 'US9368085B2', 'US8916862B2', 'US9412796B2', 'US9768237B2', 'US10133425B2', 'US10665645B2', 'US9472761B2', 'US8994396B2', 'US9224984B2', 'US10339866B2', 'US9958684B1', 'US10488959B2', 'US10990206B2', 'US10418437B1', 'US10580848B1', 'US7701135B2', 'US7750558B2', 'US9515269B2', 'US9772535B2', 'US10672838B2', 'US10861910B2', 'US8532448B1', 'US8179034B2', 'US8253328B2', 'US7629741B2', 'US8604690B2', 'US9391296B2', 'US8659558B2', 'US9507449B2', 'US10386563B2', 'US8243055B2', 'US8692742B2', 'US8084772B2', 'US8907991B2', 'US7816859B2', 'US9133119B2', 'US8294143B2', 'US8643801B2', 'US7531959B2', 'US8569774B2', 'US10438532B2', 'US10679554B2', 'US9287526B2', 'US8259095B2', 'US8299460B2', 'US8492754B2', 'US9478598B2', 'US9142802B2', 'US9099409B2', 'US9619196B2', 'US10431637B2', 'US10607538B2', 'US8599111B2', 'US9947899B2', 'US7535163B2', 'US9111892B2', 'US9647041B2', 'US10163993B2', 'US8040049B2', 'US10672340B2', 'US7510454B2', 'US8227808B2', 'US8957505B2', 'US9954036B2', 'US7776645B2', 'US7750563B2', 'US8476622B2', 'US10636848B2', 'US8384102B2', 'US9754535B2', 'US8064015B2', 'US8778712B2', 'US8384685B2', 'US8947326B2', 'US9153629B2', 'US10038034B2', 'US10056560B2', 'US9735371B2', 'US10164202B2', 'US10446776B2', 'US10403194B2', 'US8823683B2', 'US8940568B2', 'US8957579B2', 'US10545379B2', 'US9142798B2', 'US10541385B2', 'US7893609B2', 'US9773979B2', 'US10388909B2', 'US10566577B2', 'US10504976B2', 'US8575611B2', 'US9245939B2', 'US8575603B2', 'US9331128B2', 'US9812648B2', 'US10490604B2', 'US10388798B2', 'US8502757B2', 'US9502681B2', 'US8907328B2', 'US8816997B2', 'US9085929B2', 'US8847857B2', 'US10268298B2', 'US9093398B2', 'US9577014B2', 'US8442600B1', 'US9013448B2', 'US10394274B2', 'US10101833B2', 'US10693067B2', 'US7642709B2', 'US7947974B2', 'US8179336B2', 'US8223097B2', 'US8748875B2', 'US9735386B2', 'US10290829B2', 'US8232931B2', 'US9406897B2', 'US9804720B2', 'US7545350B2', 'US8013813B2', 'US8659627B2', 'US8654158B2', 'US9040967B2', 'US9698382B2', 'US9680127B2', 'US9024319B2', 'US9379350B2', 'US9285630B2', 'US9704939B2', 'US11037995B2', 'US7842406B2', 'US9209227B2', 'US9899457B2', 'US11050028B2', 'US7791271B2', 'US9063607B2', 'US9007337B2', 'US7594839B2', 'US8587003B2', 'US7957621B2', 'US7710022B2', 'US7915816B2', 'US7883386B2', 'US8118633B2', 'US10003045B2', 'US9692008B2', 'US10048795B2', 'US8368656B2', 'US7507998B2', 'US8810556B2', 'US10483492B2', 'US7666707B2', 'US8816363B2', 'US8159127B2', 'US9666829B2', 'US10804337B2', 'US7489292B2', 'US8199272B2', 'US8889474B2', 'US9171894B2', 'US8969904B2', 'US9437618B2', 'US8432381B2', 'US7944415B2', 'US8193699B2', 'US10826015B2', 'US8552641B2', 'US10658435B2', 'US7935963B2', 'US10013919B2', 'US8686634B2', 'US8809091B2', 'US9773439B2', 'US8203158B2', 'US10026905B2', 'US9345074B2', 'US9853241B2', 'US10431153B2', 'US7768019B2', 'US9978310B2', 'US9048458B2', 'US10069954B2', 'US10365774B2', 'US10649589B2', 'US10693089B2', 'US8030845B2', 'US8269755B2', 'US9305486B2', 'US8815619B2', 'US9496520B2', 'US9577210B2', 'US9818808B2', 'US9806142B2', 'US9246130B2', 'US9196666B2', 'US8535108B2', 'US9123667B2', 'US8267733B2', 'US9231036B2', 'US9034485B2', 'US9691990B2', 'US8946735B2', 'US8937632B2', 'US9305981B2', 'US9842545B2', 'US9123681B2', 'US9774007B2', 'US10452181B2', 'US8072401B2', 'US9311895B2', 'US9430968B2', 'US9419245B2', 'US9176616B2', 'US8628620B2', 'US9324268B2', 'US9842543B2', 'US8524328B2', 'US7663312B2', 'US9391122B2', 'US10115332B2', 'US7642997B2', 'US9698388B2', 'US10115332B2', 'US9978812B2', 'US8665183B2', 'US10998505B2', 'US9905773B2', 'US7636074B2', 'US8890406B2', 'US8031140B2', 'US9349957B2', 'US7561124B2', 'US9680054B2', 'US9082344B2', 'US8142251B2', 'US7538488B2', 'US7834540B2', 'US8698395B2', 'US7589461B2', 'US8736162B2', 'US9305478B2', 'US7821197B2', 'US8022900B2', 'US7579653B2', 'US7456811B2', 'US7772760B2', 'US8803415B2', 'US8344619B2', 'US8394511B2', 'US8451231B2', 'US7767474B2', 'US8797238B2', 'US8188315B2', 'US8872206B2', 'US9389715B2', 'US7772768B2', 'US9657040B2', 'US7867630B2', 'US7760430B2', 'US7683382B2', 'US7535447B2', 'US7586254B2', 'US8629842B2', 'US7960913B2', 'US7919920B2', 'US7944143B2', 'US8399270B2', 'US8409727B2', 'US8604688B2', 'US7595118B2', 'US7776457B2', 'US8872736B2', 'US7903052B2', 'US9799264B2', 'US10027951B2', 'US8258692B2', 'US8492969B2', 'US8610649B2', 'US8723024B2', 'US8558767B2', 'US8373928B2', 'US8237637B2', 'US8072150B2', 'US8415675B2', 'US8026511B2', 'US8350467B2', 'US8338832B2', 'US7688292B2', 'US8188940B2', 'US7667385B2', 'US7843126B2', 'US8698993B2', 'US8319217B2', 'US8513652B2', 'US9496321B2', 'US7910919B2', 'US7957128B2', 'US8022618B2', 'US8907324B2', 'US7995011B2', 'US7528631B2', 'US8305348B2', 'US7787168B2', 'US7719185B2', 'US7812797B2', 'US7772765B2', 'US7833633B2', 'US9178157B2', 'US9070889B2', 'US8617932B2', 'US9067885B2', 'US8633484B2', 'US8963129B2', 'US8698790B2', 'US8530910B2', 'US8226448B2', 'US8536782B2', 'US8574662B2', 'US8872797B2', 'US8188649B2', 'US8496150B2', 'US8193535B2', 'US8084940B2', 'US7961456B2', 'US7942716B2', 'US8558766B2', 'US8076704B2', 'US7950567B2', 'US8120241B2', 'US8054253B2', 'US8022616B2', 'US8031143B2', 'US7960910B2', 'US7564185B2', 'US8729796B2', 'US7834550B2', 'US8415880B2', 'US7576354B2', 'US8063853B2', 'US8018405B2', 'US7463399B2', 'US7855507B2', 'US7483004B2', 'US7940001B2', 'US7802537B2', 'US7554118B2', 'US7710366B2', 'US7705817B2', 'US7687153B2', 'US9219250B2', 'US8927120B2', 'US9287339B2', 'US9281494B2', 'US9142804B2', 'US8421743B2', 'US8987758B2', 'US8558222B2', 'US8390751B2', 'US8859306B2', 'US8409788B2', 'US8431241B2', 'US8288014B2', 'US8368297B2', 'US8138669B2', 'US8283851B2', 'US8298684B2', 'US7893440B2', 'US8710508B2', 'US8102118B2', 'US8283668B2', 'US7800110B2', 'US8174518B2', 'US7994706B2', 'US7786494B2', 'US9105237B2', 'US8149186B2', 'US7928431B2', 'US7863629B2', 'US8138568B2', 'US8547302B2', 'US7759858B2', 'US7825881B2', 'US7705530B2', 'US7692372B2', 'US8026987B2', 'US7767489B2', 'US7474061B2', 'US7795803B2', 'US7709842B2', 'US7948176B2', 'US8614655B2', 'US7843135B2', 'US7638796B2', 'US8222809B2', 'US7551255B2', 'US7915102B2', 'US7714502B2', 'US7675233B2', 'US8441420B2', 'US7864141B2', 'US7402944B2', 'US7446473B2', 'US7705810B2', 'US9341750B2', 'US8970798B2', 'US8830195B2', 'US9927641B2', 'US9172058B2', 'US8946758B2', 'US8593372B2', 'US8866170B2', 'US10057541B2', 'US8604501B2', 'US8471276B2', 'US8847246B2', 'US9761172B2', 'US9099674B2', 'US9196196B2', 'US8847940B2', 'US8481997B2', 'US8415873B2', 'US8674597B2', 'US9887020B2', 'US8587006B2', 'US8933450B2', 'US8963214B2', 'US8288784B2', 'US8524380B2', 'US8421090B2', 'US8455876B2', 'US8018406B2', 'US8018407B2', 'US8053768B2', 'US8193703B2', 'US8368299B2', 'US8253141B2', 'US7986092B2', 'US8350468B2', 'US7999457B2', 'US8933867B2', 'US7855758B2', 'US8318523B2', 'US8384701B2', 'US8378931B2', 'US8502443B2', 'US8436958B2', 'US9240487B2', 'US8169138B2', 'US8030838B2', 'US7846559B2', 'US8184074B2', 'US8587191B2', 'US8018142B2', 'US8049410B2', 'US8344969B2', 'US8129722B2', 'US8258696B2', 'US9449550B2', 'US8101979B2', 'US7915101B2', 'US8259070B2', 'US8952874B2', 'US8446555B2', 'US7868540B2', 'US8063553B2', 'US7834557B2', 'US8035298B2', 'US7893899B2', 'US7812527B2', 'US7868538B2', 'US7965272B2', 'US7834544B2', 'US7842944B2', 'US8796920B2', 'US8053779B2', 'US8711060B2', 'US7692381B2', 'US7927702B2', 'US8796918B2', 'US8120249B2', 'US7687802B2', 'US7863810B2', 'US8012527B2', 'US7863602B2', 'US8227795B2', 'US7919918B2', 'US7755585B2', 'US7710024B2', 'US8009125B2', 'US7679093B2', 'US7495716B2', 'US7629739B2', 'US8026662B2', 'US7804466B2', 'US8338222B2', 'US9590210B2', 'US8431251B2', 'US8946687B2', 'US8803866B2', 'US8785940B2', 'US8686443B2', 'US8664670B2', 'US8692346B2', 'US9614190B2', 'US8785936B2', 'US9450033B2', 'US8643019B2', 'US8698169B2', 'US9305477B2', 'US8922117B2', 'US8664021B2', 'US8525174B2', 'US9466646B2', 'US8575601B2', 'US8723764B2', 'US8258523B2', 'US8846213B2', 'US8415874B2', 'US8829495B2', 'US8836213B2', 'US8415872B2', 'US8928601B2', 'US8866378B2', 'US8736156B2', 'US8558235B2', 'US9048449B2', 'US8520182B2', 'US8513884B2']
responses = []

try:
    i = 0
    for patent in patentsToBeChecked:
        response = requests.get("http://localhost:8000/dia/generate-template/"+patent+"/1")
        responses.append(response.json())

        i+=1
        print("Processed "+str(i)+" patents")

    with open('responses.txt', 'w') as f:
        for res in responses:
            f.write(res+"\n")

except Exception as error:
    print(error)