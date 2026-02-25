input_prompt = "Welk gerecht vind je lekker?"
input_stop =  "(typ 'q' om te stoppen)"
# Initialiseer de variabele gerecht
gerecht = ""

while gerecht != "q":
    gerecht = input(input_prompt + " " + input_stop + ": ")
    if gerecht != "q":
        print(gerecht.title() + " is een lekker gerecht!")
