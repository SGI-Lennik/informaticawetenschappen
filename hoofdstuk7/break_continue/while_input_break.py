input_prompt = "Welk gerecht vind je lekker?"
input_stop =  "(typ 'q' om te stoppen)"
gerecht = ""

while True:
    gerecht = input(input_prompt + " " + input_stop + ": ")
    if gerecht == "q":
        break
    print(gerecht.title() + " is een lekker gerecht!")