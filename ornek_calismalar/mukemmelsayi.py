import time

while True:
    print("""
    ****************
    
    mukemmel sayimi ?
    
    ****************
    
    """)

    a = int(input("sayi:"))

    bolenler = []

    for i in range(1, a):

        if (a % i) == 0:
            bolenler.append(i)
            print("******* " + str(i) + " [+] sayisina bolunuyor (eklendi)")
        else:
            print(str(i) + " [-] sayisina bolunmuyor")

    print("en sonki liste:")
    print(bolenler)

    toplam = 0

    for x in bolenler:
        toplam = toplam + x

    if toplam == a:
        print("mukemmel sayi")

    else:
        print("mukemmel sayi degildir")
