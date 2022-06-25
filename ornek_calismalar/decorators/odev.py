"""

1'den 1000'e kadar olan asal sayıları ekrana yazdıran bir program yazın.
Daha sonra bir tane decorator fonksiyon kullanarak bu fonksiyona 1'den 1000'e kadar olan mükemmel sayıları yazdırma özelliği ekleyin.


"""


def extra(fonk):


    def wrapper():
        print("Mukemmel sayilar")
        for i in range(1,1001):
            bolunecek_sayi=1

            toplam = 0
            while (bolunecek_sayi<i):

                if i % bolunecek_sayi == 0:
                    toplam += bolunecek_sayi
                    bolunecek_sayi += 1
                else:
                    bolunecek_sayi += 1

            if toplam == i:
                print(i)
        fonk()
    return wrapper








@extra
def asalmi():
    print("asal sayilar")
    for i in range(2,1001):

        a = 2
        b = 0
        while (a < i):
            if i % a == 0:
                b +=1
                break

            a += 1
        if b == 0:
            print(i)
asalmi()


