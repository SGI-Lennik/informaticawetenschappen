def f(x):
    # bereken de functiewaarde van f(x) = x^2 - 2
    y = x**2-2
    return y

def nulwaarde(a,b, precisie=1E-6):
    # gebruik twee variabelen voor de nieuwe onder- en bovengrens
    ondergrens = a
    bovengrens = b
    # zolang precisie niet bereikt, halveer het interval
    while bovengrens-ondergrens > precisie:
        midden = (ondergrens+bovengrens)/2.0

        # test of de nulwaarde in het interval [midden, bovengrens] ligt
        if f(midden)*f(bovengrens) < 0:
            # pas de ondergrens aan
            ondergrens = midden
        else:
            bovengrens = midden
    # je kan de ondergrens, bovengrens of het midden teruggeven
    # ze liggen allemaal binnen de precisie van elkaar
    return ondergrens

nw = nulwaarde(1,2)
print("De nulwaarde is:\t", nw)
print("In werkelijkheid:\t", 2**0.5)
