# Maak een programma dat twee natuurlijke getallen inleest.
# Je kan een while-lus gebruiken om de gebruiker te dwingen tot correcte input
# (bijvoorbeeld negatieve waarden weigeren).
# Het programma drukt alle even getallen af,
# vanaf het kleinste van de twee getallen tot en met het grootste.
# Laat het programma bepalen welke van de twee getallen het grootste is.

# getallen inlezen
getal1 = int(input("Geef het eerste natuurlijke getal in: "))
while getal1 < 0:
    print("Het getal moet een natuurlijk getal zijn!")
    getal1 = int(input("Geef het eerste natuurlijke getal in: "))

getal2 = int(input("Geef het tweede natuurlijke getal in: "))
while getal2 < 0:
    print("Het getal moet een natuurlijk getal zijn!")
    getal2 = int(input("Geef het tweede natuurlijke getal in: "))

# getallen sorteren van klein naar groot
if getal1 < getal2:
    kleinste = getal1
    grootste = getal2
else:
    kleinste = getal2
    grootste = getal1

print("De even getallen tussen", kleinste, "en", grootste, "zijn:")

# gebruik een nieuwe variabele als teller (= netter)
# je kan ook "kleinste" gebruiken als teller (maar kan verwarrend zijn)
teller = kleinste
while teller <= grootste:
    # print even getal
    if teller % 2 == 0:
        print(teller)
    # volgende getal
    teller = teller + 1
