def binair_zoeken_iteratief(lijst, doel):
    # start met hele lijst
    index_links = 0
    index_rechts = len(lijst) - 1

    # zolang er nog een deel van de lijst over is
    while index_links <= index_rechts:
        # midden van het huidige deel van de lijst
        midden = (index_links + index_rechts) // 2

        # als het doel in het midden staat
        if lijst[midden] == doel:
            return midden
        # als het doel groter is dan het getal in het midden
        # zoek verder in het rechterdeel
        elif lijst[midden] < doel:
            index_links = midden + 1
        # anders zoek verder in het linkerdeel
        else:
            index_rechts = midden - 1

    return -1   # niet gevonden


user_ids = [14, 3, 7, 12, 2, 21, 18, 5, 9, 11, 27, 30, 17, 29, 25]
id = 21
# binair zoeken vereist een gesorteerde lijst,
# dus we sorteren de lijst eerst
user_ids_sorted = sorted(user_ids)
index = binair_zoeken_iteratief(user_ids_sorted, id)

print("Gesorteerd", user_ids_sorted)
print("User-id", id, "staat op index", index)