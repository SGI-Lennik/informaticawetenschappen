# Programma: Bioscoopticket met korting

# standaardprijs van 12 euro
standaardprijs = 12.0

# lees leeftijd
leeftijd = int(input("Hoe oud ben je? "))

# 25% korting bij leeftijd < 18 jaar
if leeftijd < 18:
    korting = 0.25
# 30% korting bij leeftijd >= 65 jaar
elif leeftijd >= 65:
    korting = 0.30
# anders geen korting
else:
    korting = 0.0
# print("DEBUG - korting:", korting)

# bereken ticketprijs
prijs = standaardprijs * (1 - korting)
# print("DEBUG - berekende prijs:", prijs)

# toon ticketprijs
print("De ticketprijs bedraagt ", prijs, "euro.")
