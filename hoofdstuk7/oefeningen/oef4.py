# Onderzoek of een natuurlijk getal,
# ingevoerd door de gebruiker,
# een priemgetal is of niet.
# Maak gebruik van een while-lus en een vlag.
# ==> met een vlag is dit algoritme niet "netjes"
# zie oef4_met_break.py voor een nettere oplossing met break

# vraag input van de gebruiker
getal = int(input("Geef een natuurlijk getal in: "))

# cnotroleer of het getal een natuurlijk getal is en niet 0
while getal <= 0:
    print("Het getal moet groter dan 0 zijn!")
    getal = int(input("Geef een natuurlijk getal in: "))

# een vlag maken als voorwaarde voor de while-lus
# we kunnen ze al gebruiken om te controleren of het getal groter dan 1 is
vlag = getal > 1
# een boolean die het resultaat bijhoudt
is_priem = getal > 1

# start bij deler 2
deler = 2

# test deling door deler tot en met getal - 1
while vlag:
    if getal % deler == 0:
        print("Geen priemgetal want deelbaar door: ", deler)
        is_priem = False
        # de vlag updaten - we kunnen stoppen met testen
        vlag = False
    else:
        # volgende deler
        deler = deler + 1
        # update vlag - we kunnen stoppen als we bij getal - 1 zijn
        vlag = deler <= getal - 1

# print het resultaat
if is_priem:
    print(getal, "is priem")
else:
    print(getal, "is niet priem")
