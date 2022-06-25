import sqlite3

import time

class Kitap():

    def __init__(self,isim,yazar,yayinevi,tur,baski):

        self.isim = isim
        self.yazar = yazar
        self.yayinevi = yayinevi
        self.tur = tur
        self.baski = baski

    def __str__(self): # yapmak istedigimiz Kitap(x,x,x,x,x) yazdirip listelemek...
        return "kitap isim ler falan filan\n{} \n{} \n{} \n{} \n{} \n".format(self.isim,self.yazar,self.yayinevi,self.tur,self.baski)


class kutupane():

    def __init__(self):

        self.baglantiolustur() #muhtemelen init fonksiyonu her classin basinda calisir yani burdada baglanti olusturma otomatikmen calisiyor...
    def baglantiolustur(self):


    #database baglanti kismi
        self.baglanti = sqlite3.connect("kütüphane.db")
        self.cursor = self.baglanti.cursor()

    #tablo olusturma

    #sorgu cumlecigi =>
        sorgu = "create table if not exists kitaplar (kitap_ismi TEXT,yazar_adi TEXT, yayin_evi TEXT, kitap_turu TEXT, baski_sayisi INT)"

        self.cursor.execute(sorgu) #sorguyu execute ettik..

        self.baglanti.commit()

    def baglantiyikes(self):

        self.baglanti.close() #baglantiyi keser

    """
    
    fonksiyonlar asagida
    
    
    """

    def kitaplari_goster(self):

        sorgu = "select * from kitaplar" #anlami su select (sec) *(all [hepsinden]) from (dan ) kitaplar / yani / kitaplardan hepsini sec ...
        self.cursor.execute(sorgu)

        sorgu_cevap = self.cursor.fetchall()

        for i in sorgu_cevap:

            if len(sorgu_cevap) == 0:

                print('hic kitap yok')

            else:

                print(Kitap(i[0],i[1],i[2],i[3],i[4],))
    def kitap_sorgu(self,aratilacak_isim):

        sorgu = "select * from kitaplar where isim = ?"

        self.cursor.execute(sorgu,(aratilacak_isim,))

        sorgu_cevap = self.cursor.fetchall()


        if len(sorgu_cevap) == 0:

            print("boyle bir kitap bulunmuyor")
        else:

            print(sorgu_cevap[0][0],sorgu_cevap[0][1],sorgu_cevap[0][2],sorgu_cevap[0][3],sorgu_cevap[0][4],)


    def kitap_ekle(self,a,b,c,d,e):

        sorgu = "insert into kitaplar values(?,?,?,?,?)"

        self.cursor.execute(sorgu,(a,b,c,d,e))
        self.baglanti.commit()

    def kitap_sil(self,a):

        sorgu = "select * from kitaplar where isim = ?"

        self.cursor.execute(sorgu, (a,))

        sorgu_cevap = self.cursor.fetchall()

        if len(sorgu_cevap) == 0:

            print("boyle bir kitap bulunmuyor")
        else:

            sorgu = "delete from kitaplar where isim = ?"



            self.cursor.execute(sorgu , (a,))
            self.baglanti.commit()












kutupane = kutupane()




while True:
    islem = input("hangi islem")
    if islem == "q":
        break
    elif islem == "1":
        kutupane.kitaplari_goster()

    elif islem == "2":
        isim = input("isim: ")
        yazar = input("yazar: ")
        yayin = input("yayin: ")
        tur = input("tur: ")
        baski= input("baski: ")

        kutupane.kitap_ekle(isim,yazar,yayin,tur,baski)
    elif islem == "3":
        sorgulanacak_isim = input("isim gir")
        kutupane.kitap_sorgu(sorgulanacak_isim)

    elif islem == "4":
        silinecek_kitap_ismi = input("silinece kitap ismi: "
                                     )
        kutupane.kitap_sil(silinecek_kitap_ismi)



