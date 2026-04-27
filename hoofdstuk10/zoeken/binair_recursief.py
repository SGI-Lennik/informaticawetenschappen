def binair_zoeken_recursief(lijst, doel, links, rechts):
    if links > rechts:
        return -1

    midden = (links + rechts) // 2

    if lijst[midden] == doel:
        return midden
    elif lijst[midden] < doel:
        return binair_zoeken_recursief(lijst, doel, midden + 1, rechts)
    else:
        return binair_zoeken_recursief(lijst, doel, links, midden - 1)

user_ids = [14, 3, 7, 12, 2, 21, 18, 5, 9, 11, 27, 30, 17, 29, 25]
id = 21
# binair zoeken vereist een gesorteerde lijst,
# dus we sorteren de lijst eerst
user_ids_sorted = sorted(user_ids)
index = binair_zoeken_recursief(user_ids_sorted, id, 0, len(user_ids_sorted) - 1)

print("Gesorteerd", user_ids_sorted)
print("User-id", id, "staat op index", index)