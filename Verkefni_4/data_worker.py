import json, random, datetime

afangar = []

with open('lib/classes/namsgagnalisti.json', 'r', encoding='UTF-8-SIG') as file:
    data = json.load(file)
    for clss in data:
        clss.pop('Námsgrein')
        clss.pop('Titill bókar')
        clss.pop('Höfundur')
        clss.pop('Útgáfuár')
        clss.pop('Útgefandi')
        clss.pop('ISBN-númer')
        afangar.append([clss['Deild'], clss['Áfangi'], clss['Heiti áfanga']])


    unique_afangar = [list(i) for i in set(tuple(i) for i in afangar)]
    unique_afangar.sort(key=lambda x: (x[0], x[1]))
    for i in unique_afangar: print(i)

    # for i in range(num):
    #     kt = ssn.ssn_generator()    # Kennitala
    #     tmp = name.name_generator() # Tímabundin breyta með nafni og kyn í lista
    #     kyn = tmp.pop()             # Kyn tekið úr tímabundna listanum sem hefur alltaf kyn sem síðasta stak
    #     nafn = " "                  # Nafn er bil til að hafa á milli nafnana þegar .join() kemur í málið
    #     nafn = nafn.join(tmp)       # Nafnið búið til af tímabundna listanum sem inniheldur eiginnafn,millinafn,eftirnafn
    #
    #     person = {'kt': kt, 'nafn': nafn, 'braut': job.job_generator(),     # Nýr einstaklingur búinn til
    #               'email': email.email_generator(kt, nafn),'kyn':kyn,
    #               'heimilisfang': heimilisfong[random.randint(0, len(heimilisfong) - 1)]}
    #     people['einstaklingar'].append(person)   # Einstaklingur settur í listann
    # json.dump(people,file, ensure_ascii=False)  # Json skrifar bekkinn í skránna að lokinni keyrslu
