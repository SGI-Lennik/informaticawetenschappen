favoriete_vakken = ["fysica", "informatica", "wiskunde", "biologie"]
minder_leuke_vakken = ["godsdienst", "frans", "nederlands"]

vak = input("Over welk vak wil je iets weten? ")
# Waarom beter kleine letters?
vak = vak.lower()

if vak in favoriete_vakken:
    print(vak.title(), "is een van mijn favoriete vakken.")
elif vak in minder_leuke_vakken:
    print(vak.title(), "is een van mijn minder favoriete vakken.")
else:
    print(vak.title(), "is zo erg nog niet.")
