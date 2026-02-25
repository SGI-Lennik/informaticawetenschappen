# Onderzoek of een natuurlijk getal,
# ingevoerd door de gebruiker,
# een priemgetal is of niet.
# Maak gebruik van een while-lus

# vraag input van de gebruiker
getal = int(input("Geef een natuurlijk getal in: "))

# cnotroleer of het getal een natuurlijk getal is en niet 0
while getal <= 0:
    print("Het getal moet groter dan 0 zijn!")
    getal = int(input("Geef een natuurlijk getal in: "))

# een boolean die het resultaat bijhoudt
is_priem = True

# geval getal 1: geen priemgetal
# is_priem op False plaatsen, de while-lus wordt toch niet uitgevoerd
if getal == 1:
    is_priem = False

# start bij deler 2
deler = 2

# test deling door deler tot en met getal - 1
while deler <= getal - 1:
    if getal % deler == 0:
        print("Geen priemgetal want deelbaar door: ", deler)
        is_priem = False
        # stop de lus!
        break

    # voorwaarde van de while-lus updaten: volgende deler
    deler = deler + 1

# print het resultaat
if is_priem:
    print(getal, "is priem")
else:
    print(getal, "is niet priem")
