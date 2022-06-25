print("""
***************************
***************************

KOKOREC ATM 

ISLEMLER:

1.Bakiye sorgulama 

2. Para yatirma

3. Para cekme

Programdan cikmak icin q ye basin...

***************************
***************************
""")

bakiye = 1000

while True:
    islem = input(
        "islemi seciniz:"
    )

    if(islem == "q"):
        print("yine bekleriz")
        break
    elif (islem == "1"):
        print("bakiyeniz:" + str(bakiye))

    elif(islem == "2"):
        yatir = int(input("ne kadar yatiracaksiniz?"))
        if(yatir > 0):
            bakiye = bakiye + yatir
        else:
            print("lutfen duzgun deger giriniz...")
        print("suanki bakiyeniz:" + str(bakiye))

    elif (islem == "3"):
        cek = int(input("ne kadar para cekeceksiniz"))
        if(cek>0 and cek < bakiye):
            bakiye = bakiye - cek
        else:
            print("aptal herif duzgun sayi yaz...")
        print("suanki bakiyeniz:" + str(bakiye))

    else:
        print("lutfen duzgun islem seciniz")








