def lineair_zoeken(lijst, doel):
    for i in range(len(lijst)):
        if lijst[i] == doel:
            return i  # index gevonden
    return -1  # niet gevonden

user_ids = [14, 3, 7, 12, 2, 21, 18, 5, 9, 11, 27, 30, 17, 29, 25]

id = 21
print("User-id", id, "staat op index", lineair_zoeken(user_ids, id))