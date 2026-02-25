# een combinatie van positionele argumenten
# en een willekeurig aantal argumenten
def som_van_getallen(start, *getallen):
    totaal = start
    for getal in getallen:
        totaal = totaal +getal
    print("De som van de getallen is:", totaal)

# functie aanroepen met 4 positionele argumenten
# "start" wordt 10, de andere positionele argumenten
# worden in de variabele "getallen" opgeslaan
som_van_getallen(10, 1, 2, 3)
