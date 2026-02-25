# twee positionele argumenten
print("Hello", "world!")
# twee positionele argumenten en een trefwoordargument (default seperator is de spatie " ")
print("Hello", "world!", sep="-")
print("Hello", "world!", sep="-", end="\n######\n")

# number of digits (ndigits): default is None (afronden op gehele getallen)
print(round(3.14159))
print(round(3.14159, ndigits=None))
# number of digits (ndigits): afronden op 2 decimalen
print(round(3.14159, ndigits=2))




print(round(111.234))