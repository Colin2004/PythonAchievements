invoer = "";
verzekering_per_maand = 23
benzine_kosten_per_liter = 1.54
liter_per_kilometer = 0.2



def maandkosten (km_per_maand):
    eindkosten = km_per_maand * benzine_kosten_per_liter * liter_per_kilometer + verzekering_per_maand
    print("Je eindkosten zijn",eindkosten)

while not isinstance(invoer, float):

    try:
        invoer = input("Hoeveel kilometer rij jij per maand? ")
        
        invoer = float(invoer)

        print("je rijd", invoer, "kilometer per maand")

    except ValueError:
        print(invoer + " is geen geldig getal!")


maandkosten(invoer)
