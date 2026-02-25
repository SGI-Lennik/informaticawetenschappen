def stel_jezelf_voor(naam, leeftijd):
    print("Mijn naam is", naam, "en ik ben", leeftijd, "jaar oud.")

# argumenten via trefwoorden
stel_jezelf_voor(naam="Arthur", leeftijd=16)

# volgorde maakt niet uit bij trefwoorden
stel_jezelf_voor(leeftijd=16, naam="Arthur")

# positionele argumenten komen altijd eerst
stel_jezelf_voor("Arthur", leeftijd=16)