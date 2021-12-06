DieselPrijs = input("Wat is de dieselprijs? ")
AantalPersonen = 4
Afstand = 244
PrijsBroodKoffie = 8

TotaalBroodKoffie = PrijsBroodKoffie * AantalPersonen
DieselVerbruik = Afstand / 12
KostenDiesel = float(DieselPrijs) * DieselVerbruik
TotaalKostenHeen = KostenDiesel + TotaalBroodKoffie
TotaalHeenTerug = TotaalKostenHeen * 2
print (TotaalHeenTerug)
# Totale Kosten 131.91