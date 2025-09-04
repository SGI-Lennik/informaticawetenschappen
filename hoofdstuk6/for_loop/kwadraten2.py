start = 1
stop = 10
print("De kwadraten van de getallen", start, "tot", stop, "zijn:")

kwadraten = [] # lege lijst om de kwadraten in op te slaan

# van start tot en met stop (inclusief stop)
for getal in range(start, stop + 1):
    kwadraat = getal ** 2
    kwadraten.append(kwadraat) # voeg het kwadraat toe aan de lijst

print(kwadraten)
