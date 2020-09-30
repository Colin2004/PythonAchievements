print("Ha..ha..hallo..da..daar..i..ik..b..ben..co...co..colin")
print("ty...ty...type hi...hi...hier onder wat je wi...wi...wilt la...la...laten st...stotteren")


running = True
while running == True:
    antwoord = input("Wat wil je laten stotteren:")
    userlist = antwoord.split()
    for x in userlist:
        if len(x) > 2:
            print(x[0:2]+"...", x[0:2]+"..." ,x)
            
        else:
            print(x)
