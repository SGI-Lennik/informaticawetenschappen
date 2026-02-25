getal = 0

while getal < 10:
    getal = getal + 1
    # Als getal even is, print niets
    if getal % 2 == 0:
        # sla deze iteratie over
        continue
    print(getal)

print("Lus is beëindigd.")
