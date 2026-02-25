# een functie die twee getallen optelt en het resultaat print
def optelling(getal_1, getal_2):
    # bereken de som
    som = getal_1 + getal_2
    # geef de berekende waarde terug aan de aanroeper
    return som

# de terugkeerwaarde gaat verloren
optelling(2, 3)

# de terugkeerwaarde wordt opgeslagen in een variabele
reultaat = optelling(2, 3)
print("De berekende som is:", reultaat)