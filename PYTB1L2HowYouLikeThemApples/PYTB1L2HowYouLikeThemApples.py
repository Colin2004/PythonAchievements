#Vervang de 0-en met de juiste berekeningen

trees               = 333             #hoeveel bomen zijn er in totaal?
shadedTrees         = trees / 3 * 2            #hoeveel bomen staan er in de schaduw (afgerond naar boven)?
sunnyTrees          = trees / 3 * 1             #hoeveel in de zon?

shadeOutputModifier = 80              #hoeveel procent productie geeft een schaduwboom?

sunnyTreeOutput     = 146                                                  #hoeveel appels geeft 1 zonnige boom?
shadedTreeOutput    = sunnyTreeOutput / 100 * shadeOutputModifier          #hoeveel appels geeft 1 schaduw boom?

sunnyOutput         = sunnyTreeOutput * sunnyTrees               #hoeveel appels geven alle zonnige bomen? 
shadedOutput        = shadedTreeOutput * shadedTrees             #hoeveel appels geven alle schaduw bomen?
totalOutput         = sunnyOutput + shadedOutput                 #hoeveel appels zijn er in totaal?

owners              = 3             #met hoeveel mensen verdelen we de appels?

eatCount            = totalOutput % owners             #hoeveel appels houden we over omdat ze niet eerlijk te verdelen zijn?
sellableOutput      = totalOutput - eatCount             #hoeveel appels zijn er over en dus verkoopbaar?
cut                 = sellableOutput / 3             #hoeveel appels mag ik verkopen?


print(trees)
print(shadedTrees)
print(sunnyTrees)
print(shadeOutputModifier)
print(sunnyTreeOutput)
print(shadedTreeOutput)
print(sunnyOutput)
print(shadedOutput)
print(totalOutput)
print(owners)
print(eatCount)
print(sellableOutput)
print(cut)