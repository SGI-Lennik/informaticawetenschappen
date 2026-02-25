def stel_jezelf_voor(naam, leeftijd):
    """
    Vertelt wie je bent en of je nog minderjarig bent.

    naam: string, de naam van de persoon
    leeftijd: integer, de leeftijd van de persoon

    Geeft een string terug zoals:
    'Mijn naam is Arthur, binnen 2 jaar word ik 18.'
    of
    'Mijn naam is Beau, ik ben meerderjarig.'
    """
    jaren_tot_18 = 18 - leeftijd

    if jaren_tot_18 > 0:
        return "Mijn naam is " + naam + ", binnen " + str(jaren_tot_18) + " jaar word ik 18."
    else:
        return "Mijn naam is " + naam + ", ik ben meerderjarig."

resulaat = stel_jezelf_voor(naam="Arthur", leeftijd=16)
print(resulaat)

resulaat = stel_jezelf_voor("Beau", leeftijd=18)
print(resulaat)