def selection_sort(lijst):
    # nieuwe lijst met elementen in de juiste volgorde
    gesorteerde_lijst = []
    while len(lijst) > 0:
        # zoek het kleinste element in de ongesorteerde lijst
        kleinste = min(lijst)
        # voeg het kleinste element toe aan de gesorteerde lijst
        gesorteerde_lijst.append(kleinste)
        # verwijder het kleinste element uit de ongesorteerde lijst
        lijst.remove(kleinste) 

    return gesorteerde_lijst

# Functie testen met lijst van getallen
willekeurige_lijst = [5, 3, 8, 9, 4, 6, 1, 7, 2]
print(selection_sort(willekeurige_lijst))

# Functie testen met lijst van strings
willekeurige_lijst = ["c", "b", "a", "A"]
print(selection_sort(willekeurige_lijst))
