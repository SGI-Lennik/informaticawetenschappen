def stel_jezelf_voor(naam, leeftijd, vak="IW"):
    print("Mijn naam is", naam, "en ik ben", leeftijd, "jaar oud.")
    print("Mijn favoriete vak is", vak)

# optioneel argument niet opgegeven, dus vak krijgt standaardwaarde "IW"
stel_jezelf_voor(naam="Arthur", leeftijd=16)

# optioneel argument opgegeven, dus vak krijgt waarde "Wiskunde"
stel_jezelf_voor(naam="Arthur", leeftijd=16, vak="Wiskunde")
