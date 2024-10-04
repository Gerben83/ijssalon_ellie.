def aanbieding_1(smaak, prijs, korting):
   
    nieuwe_prijs = prijs * (1 - korting)
    
    return (f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, "
            f"van {prijs:.2f} euro voor {nieuwe_prijs:.2f} euro.")

print(aanbieding_1('aardbei', 4, 0.1))

def inkomsten_totaal(inkomsten, btw):
    """Bereken het totaal van de inkomsten inclusief btw."""
    totaal = sum(inkomsten)
    bedrag_btw = totaal * btw
    totaal_inclusief_btw = totaal + bedrag_btw
    
    return f"Het totaal van alle inkomsten van de week is {totaal_inclusief_btw:.2f} euro, waarover {bedrag_btw:.2f} euro btw betaald dient te worden."


inkomsten_lijst = [202, 420, 125, 160, 205, 90, 345]
btw_percentage = 0.09  
resultaat = inkomsten_totaal(inkomsten_lijst, btw_percentage)
print(resultaat)

def laag_en_hoog(mijn_lijst):

    laagste = min(mijn_lijst)
    hoogste = max(mijn_lijst)
    return [laagste, hoogste]


inkomsten_lijst = [220, 430, 125, 160, 205, 90, 345]
resultaat = laag_en_hoog(inkomsten_lijst)
print("De laagste en hoogste inkomsten zijn:", resultaat)

def gemiddelde(mijn_lijst):
    """Bereken het gemiddelde van de inkomsten en retourneer als een string."""
    if len(mijn_lijst) == 0:
        return "De lijst is leeg."
    
    totaal = sum(mijn_lijst)
    gemiddeld = totaal / len(mijn_lijst)
    
    return f"De gemiddelde inkomsten deze week zijn {gemiddeld:.2f} euro."

def laag_en_hoog(mijn_lijst):
    """Bepaal de laagste en hoogste waarde in de lijst."""
    laagste = min(mijn_lijst)
    hoogste = max(mijn_lijst)
    return [laagste, hoogste]

def meervoudig(invoer_lijst):
    """Retourneer een lijst met de hoogste en laagste waarde uit de gegeven lijst."""
    if len(invoer_lijst) < 5 or len(invoer_lijst) > 10:
        return "De invoer moet tussen de 5 en 10 integers bevatten."
    
    return laag_en_hoog(invoer_lijst)

inkomsten_lijst = [220, 430, 125, 160, 205, 90, 345]
resultaat_gemiddelde = gemiddelde(inkomsten_lijst)
print(resultaat_gemiddelde)

invoer_lijst = [10, 5, 3, 2, 1, 2, 9]
resultaat_meervoudig = meervoudig(invoer_lijst)
print("De laagste en hoogste waarde zijn:", resultaat_meervoudig)
combinatie()
