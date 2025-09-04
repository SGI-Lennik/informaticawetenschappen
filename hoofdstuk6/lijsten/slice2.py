mijn_vakken = ["fysica", "informatica", "wiskunde", "biologie"]

# maak een kopie van de lijst en pas die aan
jouw_vakken = mijn_vakken[:]
jouw_vakken.remove("biologie")
jouw_vakken.append("economie")

print("Mijn favoriete vakken zijn:", mijn_vakken, sep="\n", end="\n\n")
print("Jouw favoriete vakken zijn:", jouw_vakken, sep="\n")

print("**********")

# geen kopie, maar een verwijzing
hun_vakken = mijn_vakken
hun_vakken.remove("fysica")
hun_vakken.append("LO")
# ook mijn_vakken is aangepast
print("Mijn favoriete vakken zijn:", mijn_vakken, sep="\n", end="\n\n")
print("Hun favoriete vakken zijn:", hun_vakken, sep="\n")
