"""

upgrade edilecek....


"""






import time
def nothesapla(satir):
    satir = satir[:-1] #\n sildik
    liste = satir.split(",")

    isim = liste[0]
    not1 = int(liste[1]) # listedekileri tek tek degiskene atadik
    not2 = int(liste[2])
    not3 = int(liste[3])
    ortalama = (not1+not2+not3)/3
    print("isim:",isim,"\nnot1:",not1,"\nnot2",not2,"\nnot3",not3,"\nnot ortalamasi:",str((not1+not2+not3)/3))
    print("""
***********************************************************
eklendi
***********************************************************    
        """)

    return isim ," ","ortalama --->"," ", str(ortalama)
with open("dosya.txt","r",encoding="utf-8") as file:
    ekleneceklerlist = list()
    for i in file:
        nothesapla(i)
        ekleneceklerlist.append(nothesapla(i))
    print(ekleneceklerlist)

with open("ortalamacikti.txt","w",encoding="utf-8") as file:
    print("""




'ortalamacikti.txt' adli dosya olusturuldu ve icine yaziliyor:



    
    """)
    for x in ekleneceklerlist:
        for a in x:

            print(a)
            file.write(a)
        print("**************************************")
        file.write("\n")













def kaldimi(notlar):

    notlar = notlar[:-1]

    yeniliste = notlar.split(",")

    isim = yeniliste[0]
    not1 = int(yeniliste[1])
    not2 = int(yeniliste[2])
    not3 = int(yeniliste[3])

    ortalama = (not1 + not2 + not3)/3

    return isim,ortalama






with open("dosya.txt","r",encoding="utf-8") as file:
    eklenecekler2list = list()
    for i in file:
        eklenecekler2list.append(kaldimi(i))
    print(eklenecekler2list)

with open("gecenler.txt","w",encoding="utf-8") as file:

    for d in eklenecekler2list:
        if d[1]>50:
            file.write(d[0])
            file.write("\n")



with open("kalanlar.txt", "w", encoding="utf-8") as file:
    for d in eklenecekler2list:
        if d[1] < 50:
            file.write(d[0])
            file.write("\n")















