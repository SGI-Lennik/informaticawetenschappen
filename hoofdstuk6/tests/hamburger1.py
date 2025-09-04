beschibare_toppings = ["sla", "tomaat", "kaas", "ui", "augurk"]
beschikbare_sauzen = ["ketchup", "mayonaise", "mosterd"]

gekozen_toppings = ["sla", "tomaat", "bicky uitjes"]
gekozen_sauzen = ["mayonaise"]  # meerdere sauzen mogelijk

# + operator om lijsten samen te voegen
extras = gekozen_toppings + gekozen_sauzen

# itereer over ALLE gekozen extras
for extra in extras:
    # extra aanwezig in beschikbare toppings OF sauzen?
    if extra in beschibare_toppings or extra in beschikbare_sauzen:
        print("Toevoegen:", extra)
    else:
        print("Niet beschikbaar:", extra)
