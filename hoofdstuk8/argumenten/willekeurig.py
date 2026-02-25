# een willekeurig aantal positionele argumenten
def som_van_getallen(*getallen):
    totaal = 0
    for getal in getallen:
        totaal = totaal + getal
    print("De som van de getallen is:", totaal)

# een lijst als argument doorgeven
def som_van_getallen_alternatief(getallen):
    totaal = 0
    for getal in getallen:
        totaal = totaal + getal
    print("De som van de getallen is:", totaal)

# functie aanroepen met drie positionele argumenten
som_van_getallen(1, 2, 3)
# functie aanroepen met vijf positionele argumenten
som_van_getallen(1, 2, 3, 4, 5)

# alternatief: een lijst als argument doorgeven
som_van_getallen_alternatief([1, 2, 3, 4, 5])
