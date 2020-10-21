invoer = input();
verzekering_per_maand = 23
benzine_kosten_per_liter = 1.54
liter_per_kilometer = 0.2
km_per_maand = int(invoer)


maandkosten = km_per_maand * 0,2 * 1.54 + 23


while not isinstance(invoer, float):

  
    try:
        invoer = input("Voer een getal in: ")
        invoer = float(invoer)
        print("De kosten zijn", maandkosten)

    except ValueError:
        print(invoer + " is geen geldig getal!")
