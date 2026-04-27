# Functie f(x) = x^3 - 4x^2 + 4x + 1
def f(x):
    y = x**3 - 4*x**2 + 4*x + 1
    return float(y)

# Bepaalde integraal van f(x) in [a,b]
# Trapeziumregel
def trapeziumregel(a, b, aantal_trapeziums):
    # breedte van deelinterval (hoogte trapezium)
    breedte = (b-a)/aantal_trapeziums
    # opp van alle trapeziums
    opp = 0
    # bereken de opp van elk trapezium
    for i in range(aantal_trapeziums):
        # linker- en rechtergrens van deelinterval bepalen
        linkergrens = a + i*breedte
        rechtergrens = a + (i+1)*breedte

        # opp van het i-de trapezium
        # h1 = f(linkergrens) en h2 = f(rechtergrens)
        opp_trapezium = (f(linkergrens) + f(rechtergrens)) / 2 * breedte
        # voeg oppervlakte toe
        opp = opp + opp_trapezium
    return opp

integraal = trapeziumregel(0,3,aantal_trapeziums=1000)
print(integraal)