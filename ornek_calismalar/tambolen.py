


def tambolen(sayi):
    tambolenler = list()
    sayi = int(sayi)
    for i in range(1,sayi+1):
        if (sayi % i == 0):
            tambolenler.append(i)
            print("eklendi", i)


        else:

            pass

    return tambolenler


while True:

    sex = input("sayi ya da q")

    if (sex == "q"):
        break

    else:
        sex = int(sex)
        print("tam bolen sayilar: " + str(tambolen(sex)))


