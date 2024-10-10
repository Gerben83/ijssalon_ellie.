def presenteer(inkomsten_dict, totaal):
    for key, value in inkomsten_dict.items():
        print(f"{key} : {value} euro")
    print(f"totaal : {totaal} euro")

mijn_dict = {'vis': 10, 'vlees': 25, 'overig': 15}
totaal = 50

presenteer(mijn_dict, totaal)
