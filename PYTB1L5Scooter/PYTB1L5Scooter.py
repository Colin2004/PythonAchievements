invoer = input("Hoeveel km per maand rij je?: ");
verzekering_per_maand = 23
benzine_kosten_per_liter = 1.54
liter_per_kilometer = 0.2
km_per_maand = float(invoer)


maandkosten = km_per_maand * 0.2 * 1.54 + 23


if isinstance(km_per_maand, float):

  
    try:
        print("De kosten zijn", maandkosten)

    except ValueError:
        print(invoer + " is geen geldig getal!")
