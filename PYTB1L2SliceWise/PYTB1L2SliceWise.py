
#Opdracht 1
#Haal de voornamen uit deze tekst op en maak gebruik van string slicing

stuktekst1 = "De Python lessen worden gegeven door Erik, Erwin en ook Hidde"
stuk1zondervoornaam1 = stuktekst1[37:41]
stuk1zondervoornaam2 = stuktekst1[43:48]
stuk1zondervoornaam3 = stuktekst1[56:62]

print(stuk1zondervoornaam1, stuk1zondervoornaam2, stuk1zondervoornaam3)

#Opdracht2
#Haal de namen van de vakken op uit deze tekst

stuktekst2 = "SD vakken zijn Python, UXD, Frontend development en Backend development en nog veel meer ..."
vak1 = stuktekst2[15:21]
vak2 = stuktekst2[23:26]
vak3 = stuktekst2[28:49]
vak4 = stuktekst2[52:72]

print(vak1, vak2, vak3, vak4)

#Opdracht3
#Haal de laatste zes letters uit de tekst
stukjetekst3 = "Wat is hier het laatste woord?"
laatstewoord = stukjetekst3[24:30]

print(laatstewoord)

#Opdracht4
#Haal de 5e tot en met de 8e letter op EN haal de 29e tot de 33e (dus tot niet MET de 33e) letters op uit deze tekst:
stuktekst4 = "Het www is ontwikkeld vanaf 1989 door Tim Berners-Lee"

letter5_8 = stuktekst4[4:9]
letter29tot33 = stuktekst4[28:33]

print(letter5_8, letter29tot33)

