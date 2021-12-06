PemmicanRepenPersoon = 6
VijgenPlakkenPersoon = 3
AantalscheepsbiscuitRollen = 2
AantalFireSteels = 2
AantalPakjesLucifers = 5
AantalVuurStenen = 4
AantalSisatouw = 1
AantalPersonen = 4

PrijsPemmicanRepen = float(input("Hoeveel kost een pakje Pemmican-Repen? "))
PrijsVijgenPlak = float(input("Hoeveel kost een VijgenPlak? "))
PrijsScheepsBiscuitRol = float(input("Hoeveel kost een scheepsbiscuit rol? "))
PrijsFireSteel = float(input("Hoeveel kost een firesteel? "))
PrijsPakjeLucifers = float(input("Hoeveel kost een pakje lucifers? "))
PrijsVuurSteen = float(input("Hoeveel kost een originele vuursteen? "))
PrijsSisalTouw2Meter = float(input("Hoeveel kost een sisaltouw per 2 meter? "))
 
TotaalPrijsPemmicanRepen = PemmicanRepenPersoon * AantalPersonen / 4 * PrijsPemmicanRepen
TotaalPrijsVijgenPlak = VijgenPlakkenPersoon * 4 * PrijsVijgenPlak
TotaalPrijsScheepsBiscuits = PrijsScheepsBiscuitRol * AantalscheepsbiscuitRollen
TotaalPrijsFireSteel = AantalFireSteels * PrijsFireSteel
TotaalPrijsPakjeLucifers = AantalPakjesLucifers * PrijsPakjeLucifers
TotaalPrijsVuurSteen = AantalVuurStenen * PrijsVuurSteen
TotaalPrijsSisalTouw = PrijsSisalTouw2Meter * 10
TotaalPrijsAlles = TotaalPrijsPemmicanRepen + TotaalPrijsVijgenPlak + TotaalPrijsScheepsBiscuits + TotaalPrijsFireSteel + TotaalPrijsPakjeLucifers + TotaalPrijsVuurSteen + TotaalPrijsSisalTouw
print (TotaalPrijsAlles)