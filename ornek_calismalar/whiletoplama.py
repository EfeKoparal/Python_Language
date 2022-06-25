
toplam = 0
while True:

    a = input(
        "sayi veya q giriniz: "


    )

    if a == "q":
        print(toplam)
        break
    else:

        toplam = toplam + int(a)

