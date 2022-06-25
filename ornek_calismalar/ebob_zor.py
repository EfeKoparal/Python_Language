while True:
    sayi1 = int(input("sayi 1 : "))
    sayi2 = int(input("sayi 2 : "))
    ortakliste = list()


    def bolenbulma(sayi):
        geciciliste = list()
        for i in range(1, sayi + 1):
            if (sayi % i == 0):
                geciciliste.append(i)

        return geciciliste


    for x in bolenbulma(sayi1):
        for a in bolenbulma(sayi2):
            if (x == a):
                ortakliste.append(a)

    enbuyuk = 0
    for k in ortakliste:
        if k > enbuyuk:
            enbuyuk = k
    print("ebob = " + str(enbuyuk))


