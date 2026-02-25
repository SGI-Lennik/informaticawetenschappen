# een functie die twee getallen optelt en het resultaat print
def optelling(getal_1, getal_2):
    som = getal_1 + getal_2
    print(som)

print("Geef twee getallen op en ik zal de som berekenen.")
getal_1 = int(input("Voer het eerste getal in: "))
getal_2 = int(input("Voer het tweede getal in: "))

# functie aanroepen met argumenten
optelling(getal_1, getal_2)