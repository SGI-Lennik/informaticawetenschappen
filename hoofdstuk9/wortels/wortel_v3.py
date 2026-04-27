def derdemachtswortel(getal):
    if getal >= 0:
        for i in range(getal+1):
            uitkomst = i**3
            if uitkomst == getal:
                return i
            elif uitkomst > getal:
                print("Het gegeven getal", getal, "heeft geen geheel getal als derdemachtswortel")
                return None
    else:
        for i in range(abs(getal)+1):
            uitkomst = (-1*i)**3
            if uitkomst == getal:
                # de wortel van een negatief getal is negatief, dus we geven -i terug
                return -i
            # de logica draait hier om!
            elif uitkomst < getal:
                print("Het gegeven getal", getal, "heeft geen geheel getal als derdemachtswortel")
                return None        

getal = -8
wortel = derdemachtswortel(getal)
if wortel is not None:
    print("De derdemachtswortel van", getal, "is", wortel)
else:
    print("Er is geen gehele derdemachtswortel gevonden voor", getal)