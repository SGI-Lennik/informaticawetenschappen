vakken = ["fysica", "informatica", "wiskunde", "economie"]
print(vakken)

# verwijder index 2 "wiskunde" uit de lijst
del vakken[2]
print(vakken)

# verwijder index 2 uit de lijst en geef de waarde terug
verwijderd_vak = vakken.pop(2)
print("verwijderd vak:", verwijderd_vak)
print(vakken)

# verwijder "fysica" uit de lijst
vakken.remove("fysica")
print(vakken)

# verwijder "informatica" uit de lijst m.b.v. variabele
informatica = "informatica"
vakken.remove(informatica)
print(vakken)
