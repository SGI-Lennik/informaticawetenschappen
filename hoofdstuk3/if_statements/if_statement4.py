# score van leerling (integer)
punten = 75

# if-blok met meerdere voorwaarden
# print beoordeling op basis van score
if punten >= 90:
    # meer dan 89
    print("Uitstekend")
elif punten >= 70:
    # meer dan 69, maar minder dan 90
    print("Goed")
elif punten >= 50:
    # meer dan 49, maar minder dan 70
    print("Voldoende")
else:
    # minder dan 50
    print("Onvoldoende")