# Initialiseer altijd variabelen die je
# in een while-lus gebruikt om data op te slaan
totaal_rood = 0
totaal_blauw = 0

boodschap_gooien = "Elke speler gooit met een dobbelsteen..."
prompt_rood = "Aantal ogen op de rode dobbelsteen: "
prompt_blauw = "Aantal ogen op de blauwe dobbelsteen: "

vlag = True

while vlag:
    # Gebruikers resultaten laten invoeren
    print(boodschap_gooien)
    rode_dobbelsteen = int(input(prompt_rood))
    blauwe_dobbelsteen = int(input(prompt_blauw))

    # Totalen bijwerken
    totaal_rood = totaal_rood + rode_dobbelsteen
    totaal_blauw = totaal_blauw + blauwe_dobbelsteen

    print("Rode speler staat nu op: " + str(totaal_rood))
    print("Blauwe speler staat nu op: " + str(totaal_blauw))

    # Vlag aanpassen als een speler gewonnen heeft
    if totaal_rood == totaal_blauw and totaal_rood >= 20:
        print("Gelijkspel! Nog een rondje!")
    elif totaal_rood >= 20:
        print("Rode speler heeft gewonnen!")
        vlag = False
    elif totaal_blauw >= 20:
        print("Blauwe speler heeft gewonnen!")
        vlag = False