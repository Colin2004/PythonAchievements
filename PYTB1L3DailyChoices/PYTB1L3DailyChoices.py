print("Je word wakker wat da je als eerst?")

Keuze = input("Ga je lekker douchen of eerst ontbijten? ")

if Keuze == "douchen" :
    print("Je begint de dag lekker schoon.")
elif Keuze == "ontbijten" :
    print("Je begint de dag graag met een volle maag.")
else:
    print("Helaas dat is geen geldig antwoord.")

print("")

print("Je moet naar school. Hoe ga je er heen?")

Keuze2 = input("Pak je de bus of trein? ")

if Keuze2 == "bus":
    print("Je besluit om met de bus naar school te gaan.")
elif Keuze2 == "trein":
    print("Je besluit om met de trein te gaan.")
else:
    print("Helaas dat is geen geldig antwoord.")

print("")

print("Eenmaal op school volg je een heel erg saaie les wat doe je?")
Keuze3 = input("Ga je een game spelen of opletten? ")

if Keuze3 == "een game spelen":
    print("Je hebt geen zin in de les en besluit een game te spelen.")
    print("Helaas heb je nuttige informatie gemist.")
elif Keuze3 == "opletten":
    print("Je besluit alsnog op te letten waardoor je de stof goed begrijpt.")
else:
    print("Helaas dat is geen geldig antwoord.")

print("")

print("Eenmaal thuis zit je te twijfelen wat je gaat doen.")

Keuze4 = input("Ga je huiswerk maken of een film kijken? ")

if Keuze4 == "huiswerk maken":
    print("Je besluit aan je huiswerk te zitten zodat je goed voorbereid bent.")
elif Keuze4 == "een film kijken":
    print("Je gaat een ander keer aan je huiswerk en besluit een film te kijken.")
else:
    print("Helaas dit is geen geldig antwoord.")

print("")

print("Je bent moe maar je hebt nog wat dingen te doen wat doe je?")

Keuze5 = input("Ga je slapen of ga je aan het werk? ")

if Keuze5 == "slapen":
    print("Je vind dat je genoeg energie nodig hebt voor morgen en gaat slapen.")
elif Keuze5 == "aan het werk":
    print("Je besluit tot laat in de avond het werk af te maken.")
else:
    print("Helaas dit is geen geldig antwoord.")

