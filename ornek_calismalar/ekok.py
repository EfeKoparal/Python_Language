def ekokbulma(sayi1,sayi2):
    i = 2
    ekok = 1
    while True:

        if (sayi1 % i == 0) and (sayi2 % i == 0):

            ekok *= i
            sayi1 //=i
            sayi2 //=i

        elif (sayi1 % i == 0) and (sayi2 % i != 0):
            ekok *= i
            sayi1 //=i


        elif (sayi1 % i != 0) and (sayi2 % i == 0):
            ekok *= i
            sayi2 //= i
        else:

            i +=1
        if(sayi1 ==1 and sayi2 ==1):
            break

    return ekok

sayi1 = int(input("sayi 1 : "))
sayi2 = int(input("sayi 2 : "))

print("ekok:", ekokbulma(sayi1,sayi2))
