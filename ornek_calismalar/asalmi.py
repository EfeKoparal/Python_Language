"""

asal sayilar : 1 e ve kendisinden baska sayiya bolunmeyen sayilardir.

"""

import time

def asalmi(sayi):
    if sayi == 1:
        return False

    elif sayi == 2:
        return True
    else:
        for i in range(2,sayi):

            if(sayi % i == 0):
                print("ilk bolunen sayi: " + str(i))
                return False
                break

            elif(sayi % i != 0):
                if((sayi-1) != i):
                    print("deneniyor... " + str(i))
                elif((sayi-1) == i):
                    return True

while True:
    sayi = input("sayi gir: ")

    if (sayi == "q"):
        break
    else:
        sayi = int(sayi)

        if (asalmi(sayi)):
            print("""
************************************
{}, "sayimiz asal bir sayidir
            
Yeni sayi girin
            
************************************
            """.format(sayi))
        else:
            print("""
************************************
{}, sayimiz asal bir sayi degildir
                        
Yeni sayi girin
                        
************************************
                        """.format(sayi))

