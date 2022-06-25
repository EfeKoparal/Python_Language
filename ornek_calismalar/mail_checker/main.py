import time

def etvarmi(x):
    print("""

**************************
fonksiyon 1: @ varmi ?
**************************
    
    """)
    for a in x:
        print("deneniyor...")
        time.sleep(0.5)
        if a == "@":
            print("buldu")
            return True

    return False


def etcounter(x):
    print("""
*******************
fonksiyon 2: kac tane @ var
******************* 
    
    """)


    count = 0
    for i in x:
        time.sleep(0.5)
        print("deneniyor...")
        if i == "@":
            print("buldu")
            count += 1

    if count > 1:

        return False
    else:
        print("sikinti cikmadi")
        return True

def etbastami(x):
    print("""
*******************
fonksiyon 3: @ basta mi sorgusu
*******************
    
    """)
    counter = 0
    for a in x:
        print("denendi")
        time.sleep(0.5)
        if counter == 0 and x == "@":

            return False
        else:
            print("@ basta degil fonksiyon True")
            return True
def etten_sonra_nokta_varmi(x):
    print("""
*******************
fonksiyon 4: @ ten sonra nokta varmi
*******************
    """)


    counter = 0
    et_index = x.find("@")

    bosliste = list()
    for a in x:

        print("@ ten sonrakiler listeye aktariliyor...")
        time.sleep(0.5)
        if counter > et_index:
            bosliste.append(a) #@ dan sonraki karakterleri boslisteye ekledik
        counter += 1

    nokta_sayisi =0 # eger nokta sayisi 1 i gecerse return false
    for i in bosliste:
        print("deneniyor")
        time.sleep(0.5)
        if i == ".":
            print("nokta bulundu")
            nokta_sayisi +=1

    if nokta_sayisi > 1:
        return False
    else:
        print("sadece 1 tane nokta var gecti")
        return True
def etten_sonra_sayi_varmi(x):
    print("""
*******************
fonksiyon 5: @ ten sonra sayi var mi
*******************
    """)
    counter = 0
    et_index = x.find("@")

    bosliste = list()

    for a in x:
        time.sleep(0.5)
        if counter > et_index:
            print("@ten sonraki sayilar listeye ekleniyor...")
            bosliste.append(a)  # @ dan sonraki karakterleri boslisteye ekledik
        counter += 1

    for i in bosliste:
        print("deneniyor")
        time.sleep(0.5)
        if (i == "0") or (i == "1") or (i == "2") or (i == "3") or (i == "4") or (i == "5") or (i == "6") or (i == "7") or (i == "8") or (i == "9"):
            print("sayi bulundu!")
            return False
        else:

            pass
    print("sayi bulunmadi fonksiyon True")
    return True











mail = input("Mail adresinizi giriniz:")

if etcounter(mail) and etvarmi(mail) and etbastami(mail) and etten_sonra_nokta_varmi(mail) and etten_sonra_sayi_varmi(mail):
    print("*****************************")
    print(mail, "bir maildir")
else:
    print(mail, "bir mail degildir.")

