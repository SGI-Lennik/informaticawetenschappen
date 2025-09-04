getallen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# eerste 5 elementen
print(getallen[0:5])

# eerste 3 elementen - geen start
print(getallen[:3])

# getallen 3 (index 2) tot en met 7 (index 6)
print(getallen[2:7])

# getallen vanaf 6 (index 5) tot het einde - geen einde
print(getallen[5:])

kopie = getallen[:]
print("Kopie van de lijst:", kopie)

# even getallen
# start op index 1, stapgrootte 2
even = getallen[1::2]
print("Even getallen:", even)
