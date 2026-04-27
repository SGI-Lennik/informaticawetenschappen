# functie definiëren met parameter "getal"
def vierkantswortel(getal):
    # iteratief zoeken naar de wortel van een getal
    # for-lus start bij 0 en gaat door tot het getal zelf    
    for i in range(getal+1):
        # variabele die kwadraat van i bijhoudt
        uitkomst = i**2
        # conditionele test: is i^2 gelijk aan het gegeven getal
        if uitkomst == getal:
            # geef i terug als de wortel van het getal
            # de lus stopt hier omdat we de wortel hebben gevonden
            return i

    # geen wortel gevonden
    print(getal, "heeft geen geheel getal als positieve wortel")
    # geef None terug als er geen wortel is gevonden
    return None

getal = 15129
wortel = vierkantswortel(getal)
if wortel is not None:
    print("De positieve wortel van", getal, "is", wortel)
else:
    print("Er is geen gehele positieve wortel gevonden voor", getal)