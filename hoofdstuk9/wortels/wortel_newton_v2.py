def vierkantswortel(getal):
    # variabele die de gok bijhoudt, we beginnen met 1
    gok = 1
    # precisie vastleggen
    precisie = 0.001

    # zolang gok^2 te ver ligt van het gegeven getal, nieuwe gok berekenen
    while abs(gok**2-getal) > precisie:
        # nieuwe gok berekenen
        gok = (gok + getal/gok)/2
        print("DEBUG - gok:", gok, "gok^2:", gok**2)
    # de while-lus stop als de precisie is bereikt
    return gok

wortel = vierkantswortel(16)
print("De vierkantswortel van 16 is ongeveer", wortel)
