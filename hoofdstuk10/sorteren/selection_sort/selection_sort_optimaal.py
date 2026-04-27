def selection_sort(lijst):
    n = len(lijst)
    
    # n-1 stappen nodig om lijst te sorteren
    for i in range(n-1):
        # Zoek de index van het kleinste element in ongesorteerd deel.
        index_kleinste = i # start met zoeken vanaf index i, de rest is gesorteerd
        
        # Controleer alle elementen op index j (vanaf i+1).
        for j in range(i+1, n):
            # Kleiner element gevonden? update index_kleinste.
            if lijst[j] < lijst[index_kleinste]:
                index_kleinste = j

        # Verwissel het kleinste element op index index_kleinste met
        # het eerste element van de ongesorteerde lijst op index i.
        # Enkel nodig als het kleinste element nog niet juist staat.
        if index_kleinste != i:
            tijdelijk = lijst[i]
            lijst[i] = lijst[index_kleinste]
            lijst[index_kleinste] = tijdelijk

    # Geen return nodig, de lijst wordt in-place gesorteerd.

# Functie testen met lijst van getallen
willekeurige_lijst = [5, 3, 8, 9, 4, 6, 1, 7, 2]
selection_sort(willekeurige_lijst)
print(willekeurige_lijst)

# Functie testen met lijst van strings
willekeurige_lijst = ["c", "b", "a", "A"]
selection_sort(willekeurige_lijst)
print(willekeurige_lijst)
