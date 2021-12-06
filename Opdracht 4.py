# Totaalprijs 195,22
def NietInAanmerking():
    print ("U komt helaas niet in aanmerking.")
VraagLeeftijd = int(input("Hoe oud bent u? "))
VraagFlexibel = int(input("Op een schaal van 1 tot 10 hoe flexibel bent u? (1 is totaal niet en 10 heel erg) "))
VraagPositief = int(input("Op een schaal van 1 tot 10 hoe positief bent u? (1 is totaal niet en 10 heel erg) "))
VraagDoorzettend = int(input("Op een schaal van 1 tot 10 hoe doorzettend bent u? (1 is totaal niet en 10 heel erg) "))

if VraagLeeftijd > 16 and VraagFlexibel > 5 and VraagPositief > 5 and VraagDoorzettend > 5:
    # De Beer
    VraagKracht = int(input("Op een schaal van 1 tot 10 hoeveel kracht heeft u? (1 is totaal niet en 10 heel veel) "))
    VraagUithoudingsVermogen = int(input("Op een schaal van 1 tot 10 hoeveel uithoudingsvermogen heeft u? (1 is totaal niet en 10 heel veel) "))
    # De Vos
    VraagProbleemOplossing = int(input("Op een schaal van 1 tot 10 hoe goed bent u in problemen oplossen? (1 is totaal niet goed en 10 heel erg) "))
    VraagVangenDieren = int(input("Op een schaal van 1 tot 10 hoe goed ben je in het vangen van dieren? (1 is totaal niet en 10 heel erg) "))
    # De Bever
    VraagMaterialenMaken = int(input("Op een schaal van 1 tot 10 hoe goed ben je in het bewerken van materialen? (1 is totaal niet en 10 heel erg) "))
    VraagMakenHutten = int(input("Op een schaal van 1 tot 10 hoe goed ben je in het constructueren van hutten? (1 is totaal niet en 10 heel erg) "))
    # De Uil
    VraagNatuurlijkeMaterialen = int(input("Op een schaal van 1 tot 10 heb je veel kennis over natuurlijke materialen? (1 is totaal niet en 10 heel veel)"))
    VraagWaterZuiveren = int(input("Op een schaal van 1 tot 10 hoeveel kennis heb je over het zuiveren van water? (1 is totaal niet en 10 heel veel"))

    VraagGeldBijleggen = float(input("Hoeveel geld bent u bereid bij te leggen voor dit avontuur? "))

    if VraagGeldBijleggen >= 39.04:
        if VraagKracht >= 6 and VraagUithoudingsVermogen >= 6:
            print ("U komt in aanmerking om de beer te zijn")
        if VraagProbleemOplossing >= 6 and VraagVangenDieren >= 6:
            print ("U komt in aanmerking om de vos te zijn")
        if VraagMaterialenMaken >= 6 and VraagMakenHutten >= 6:
            print ("U komt in aanmerking om de bever te zijn")
        if VraagNatuurlijkeMaterialen >= 6 and VraagWaterZuiveren >= 6:
            print ("U komt in aanmerking om de uil te zijn")
    else:
        NietInAanmerking()