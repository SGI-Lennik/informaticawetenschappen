def vierkantswortel(getal):
    for i in range(getal+1):
        uitkomst = i**2
        if uitkomst == getal:
            return i
        # conditionele test: is i^2 groter dan het gegeven getal?
        elif uitkomst > getal:
            # geen wortel gevonden
            print(getal, "heeft geen geheel getal als positieve wortel")
            # stop de lus en de functie door None terug te geven
            return None

getal = 15400
wortel = vierkantswortel(getal)
if wortel is not None:
    print("De positieve wortel van", getal, "is", wortel)
else:
    print("Er is geen gehele positieve wortel gevonden voor", getal)