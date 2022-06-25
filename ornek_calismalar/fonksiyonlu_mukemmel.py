

def mukemmelmi(sayi):
    toplamliste = list()
    global ikincilist
    for i in range(1,sayi):
        if (sayi % i == 0):

            toplamliste.append(i)


    toplamcikti = 0


    ikincilist = toplamliste


    for x in toplamliste:
        toplamcikti = toplamcikti + x



    if toplamcikti == sayi:
        return True
    else:
        return False


for x in range(0,1000):

    if mukemmelmi(x):
        print(str(x) + " mukemmel sayidir..." + str(ikincilist))
    else:
        print(str(x) + " mukemmel sayi degildir...")

