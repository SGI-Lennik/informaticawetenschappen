# Functie f(x) = x^3 - 4x^2 + 4x + 1
def f(x):
    y = x**3 - 4*x**2 + 4*x + 1
    return float(y)

# Bepaalde integraal van f(x) in [a,b]
def trapeziumregel_optimalisatie(a, b, aantal_trapeziums):
    # breedte van deelinterval (hoogte trapezium)
    breedte = (b-a)/aantal_trapeziums
    som_functiewaarden = 0.0
    # tel alle hoogtes van de trapeziums bij elkaar op
    # behalve de eerste en de laatste
    for i in range(aantal_trapeziums-1):
        rechtergrens = a + (i+1)*breedte
        som_functiewaarden = som_functiewaarden + f(rechtergrens)
    
    opp = (som_functiewaarden + (f(a) + f(b))/2) * breedte
    return opp

integraal = trapeziumregel_optimalisatie(0,3,aantal_trapeziums=1000)
print(integraal)