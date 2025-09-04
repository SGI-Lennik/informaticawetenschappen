beschibare_toppings = ["sla", "tomaat", "kaas", "ui", "augurk"]
beschikbare_sauzen = ["ketchup", "mayonaise", "mosterd"]

gekozen_toppings = ["sla", "tomaat", "bicky uitjes"]
gekozen_sauzen = ["mosterd"]  # meerdere sauzen mogelijk

kostprijs = 3.00 # basisprijs hamburger
toegevoegde_extras = []  # lijst om toegevoegde extras bij te houden

# + operator om lijsten samen te voegen
extras = gekozen_toppings + gekozen_sauzen

# itereer over ALLE gekozen extras
for extra in extras:
    # extra aanwezig in beschikbare toppings OF sauzen?
    if extra in beschibare_toppings or extra in beschikbare_sauzen:
        print("Toevoegen:", extra)
        kostprijs = kostprijs + 0.50
        toegevoegde_extras.append(extra)
    else:
        print("Niet beschikbaar:", extra)

# print de rekening, inclusief toegevoegde extras
print("\nRekening:", end="\n\n")    # twee nieuwe regels
print("Hamburger\t€ 3.00")          # \t is een tab voor mooie uitlijning
for extra in toegevoegde_extras:
    print("Extra", extra, "\t€ 0.50")
print("-----------------------")
print("Totaal\t\t€", kostprijs)
print("-----------------------")
print("Bedankt voor uw bestelling!")

