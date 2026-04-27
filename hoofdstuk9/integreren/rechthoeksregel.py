# Functie f(x) = x^3 - 4x^2 + 4x + 1
def f(x):
    y = x**3 - 4*x**2 + 4*x + 1
    return float(y)

# Bepaalde integraal van f(x) in [a,b]
# Rechthoeksregel m.b.v. functiewaarde in het midden van de rechthoeken
def rechthoeksregel(a, b, aantal_rechthoeken):
    # breedte van basis van rechthoeken
    breedte = (b-a)/aantal_rechthoeken
    # verschuiving naar het midden van het interval
    offset = breedte/2
    # opp van alle rechthoeken
    opp = 0
    # bereken de opp van elke rechthoek
    for i in range(aantal_rechthoeken):
        # opp van de i-de rechthoek
        # breedte * functiewaarde in het midden van de rechthoek
        opp_rechthoek = breedte * f(a + offset + i*breedte)
        # voeg oppervlakte toe
        opp = opp + opp_rechthoek
    return opp

integraal = rechthoeksregel(a=0, b=3, aantal_rechthoeken=3)
print(integraal)
