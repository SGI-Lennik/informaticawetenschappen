def stel_jezelf_voor(naam, leeftijd):
    print("Mijn naam is", naam, "en ik ben", leeftijd, "jaar oud.")

# argumenten worden op volgorde doorgegeven
stel_jezelf_voor("Arthur", 16)

# logische fout: argumenten staan in verkeerde volgorde
stel_jezelf_voor(16, "Arthur")

# runtime fout: te weinig argumenten
stel_jezelf_voor("Arthur")