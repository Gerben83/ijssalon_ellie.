#Huiswerkopdracht Les 7
prijzen = { # 1.2
    "aardbei": 3, 
    "vanille": 4,
    "chocolade" : 5 
    }
aanbieding = prijzen["aardbei"] * 0.8 #1.3
reclame_tekst = f"Vandaag in de aanbieding: aardbei-ijs, 1 liter - slechts €{aanbieding}" #1.4
reclame_tekst2 = reclame_tekst[:62]  #1.5
reclame_tekst3 = reclame_tekst2.upper() #1.6
reclame_tekst4 = reclame_tekst3.split() #1.7
for el in reclame_tekst4: #1.8
    print(el.lower()) #1.9
    for el in reclame_tekst4:
        if len(el) > 4:
            print(el.upper())
        else:
            print (el.lower())