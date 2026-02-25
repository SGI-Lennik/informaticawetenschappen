# een functie die twee getallen optelt en het resultaat print
def optelling(getal_1, getal_2):
    som = getal_1 + getal_2
    print(som)

# een variabele buiten de functie
getal_1 = 0

# functie aanroepen met verschillende argumenten
# getal_1 in de functie krijgt waarde 2
optelling(2, 3)

# de variabele buiten de functie is ongewijzigd
print(getal_1)
