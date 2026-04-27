# Functie f(x) = x^3 - 4x^2 + 4x + 1
def f(x):
    y = x**3 - 4*x**2 + 4*x + 1
    return float(y)

# Functie g(x) = x^2 + 2x + 3
def g(x):
    return float(x**2 + 2*x + 3)

print("f(1)=", f(1))
print("g(1)=", g(1))