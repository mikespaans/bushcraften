# Totaalprijs 195,22
def NietInAanmerking():
    print ("U komt helaas niet in aanmerking.")
VraagLeeftijd = int(input("Hoe oud bent u? "))
VraagFlexibel = int(input("Op een schaal van 1 tot 10 hoe flexibel bent u? (1 is totaal niet en 10 heel erg) "))
VraagPositief = int(input("Op een schaal van 1 tot 10 hoe positief bent u? (1 is totaal niet en 10 heel erg) "))
VraagDoorzettend = int(input("Op een schaal van 1 tot 10 hoe doorzettend bent u? (1 is totaal niet en 10 heel erg) "))

if VraagLeeftijd > 16 and VraagFlexibel > 5 and VraagPositief > 5 and VraagDoorzettend > 5:
    # De Beer
    VraagKracht = int(input("Hoeveel KG kunt u drukken? "))
    VraagSpijkerBuigen = int(input("wat is de dikste spijker die u kunt buigen in mm? "))
    # De Vos
    VraagIQ = int(input("Wat is uw IQ? "))
    VraagKastInElkaar = int(input("Binnen hoeveel seconden kunt u een IKEA Larsfrid kast in elkaar zetten? "))
    # De Bever
    VraagSlotenSpringen = int(input("Wat is de grootste sloot waar u over heen kan springen in meters? "))
    VraagVuurMaken = int(input("Binnen hoeveel seconden kunt u vuur maken met vuurstenen en hooi? "))
    # De Uil
    VraagEetbarePaddeStoelen = int(input("Hoeveel eetbare paddestoelen kunt u herkennen?"))
    VraagGiftigeKruiden = int(input("Hoeveel giftige kruiden kunt u herkennen"))

    VraagGeldBijleggen = float(input("Hoeveel geld bent u bereid bij te leggen voor dit avontuur? "))

    if VraagGeldBijleggen >= 39.04:
        if VraagKracht >= 100 and VraagSpijkerBuigen >= 10:
            print ("U komt in aanmerking om de beer te zijn")
        if VraagIQ >= 130 and VraagKastInElkaar <= 300:
            print ("U komt in aanmerking om de vos te zijn")
        if VraagSlotenSpringen >= 3 and VraagVuurMaken <= 60:
            print ("U komt in aanmerking om de bever te zijn")
        if VraagEetbarePaddeStoelen >= 10 and VraagGiftigeKruiden >= 20:
            print ("U komt in aanmerking om de uil te zijn")
        else:
            NietInAanmerking()
    else:
        NietInAanmerking()