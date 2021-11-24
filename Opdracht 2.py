PemmicanRepenPersoon = 6
VijgenPlakkenPersoon = 3
AantalscheepsbiscuitRollen = 2
AantalFireSteels = 2
AantalPakjesLucifers = 5
AantalVuurStenen = 4
AantalSisatouw = 1
AantalPersonen = 4

PrijsPemmicanRepen = int(input("Hoeveel kost een pakje Pemmican-Repen? "))
PrijsVijgenPlak = int(input("Hoeveel kost een VijgenPlak? "))
PrijsScheepsBiscuitRol = int(input("Hoeveel kost een scheepsbiscuit rol? "))
PrijsFireSteel = int(input("Hoeveel kost een firesteel? "))
PrijsPakjeLucifers = int(input("Hoeveel kost een pakje lucifers? "))
PrijsVuurSteen = int(input("Hoeveel kost een originele vuursteen? "))
PrijsSisalTouw2Meter = int(input("Hoeveel kost een sisaltouw per 2 meter? "))
 
TotaalPrijsPemmicanRepen = PemmicanRepenPersoon * AantalPersonen / 4 * PrijsPemmicanRepen
TotaalPrijsVijgenPlak = VijgenPlakkenPersoon * 4 * PrijsVijgenPlak
TotaalPrijsScheepsBiscuits = PrijsScheepsBiscuitRol * AantalscheepsbiscuitRollen
TotaalPrijsFireSteel = AantalFireSteels * PrijsFireSteel
TotaalPrijsPakjeLucifers = AantalPakjesLucifers * PrijsPakjeLucifers
TotaalPrijsVuurSteen = AantalVuurStenen * PrijsVuurSteen
TotaalPrijsSisalTouw = PrijsSisalTouw2Meter * 10
TotaalPrijsAlles = TotaalPrijsPemmicanRepen + TotaalPrijsVijgenPlak + TotaalPrijsScheepsBiscuits + TotaalPrijsFireSteel + TotaalPrijsPakjeLucifers + TotaalPrijsVuurSteen + TotaalPrijsSisalTouw
print (TotaalPrijsAlles)