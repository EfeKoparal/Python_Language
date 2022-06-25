def extra(fonk):

    def wrapper(sayilar):

        ciftler_toplami = 0
        cift_sayilar = 0
        tekler_toplami = 0
        tek_sayilar = 0

        for sayi in sayilar:
            if (sayi % 2 == 0):

                ciftler_toplami += sayi
                cift_sayilar += 1

            else:

                tek_sayilar += 1
                tekler_toplami +=sayi
        print("cift sayilarin ortalamasi: {} / {} = ".format(ciftler_toplami,cift_sayilar) + str(ciftler_toplami / cift_sayilar))
        print("tek sayilarin ortalamasi: {} / {} = ".format(tekler_toplami,tek_sayilar) + str(tekler_toplami/tek_sayilar))
        fonk(sayilar) # bunu cikarirsan asil fonksiyon calismaz...
    return wrapper
@extra
def ortalama_bul(sayilar):

    toplam = 0

    for i in sayilar:

        toplam += i

    print("Ortalama : {} / {} = ".format(toplam,len(sayilar)) + str(toplam/ len(sayilar)))

ortalama_bul([1,2,4,67,2,8,4])
