"""

gelistirelecek
"""

class Dosya():

    def __init__(self):
        self.ucuncufonklist = dict()
        with open("metin.txt","r",encoding="utf-8") as file:

            dosya_icerigi =file.read()

            kelimeler = dosya_icerigi.split()
            self.sade_kelimeler = list()

            for i in kelimeler:
                i = i.strip("\n")
                i = i.strip(".")
                i = i.strip(",")
                i = i.strip(" ")
                self.sade_kelimeler.append(i)

    def tumkelimeler(self):

        kelimeler_kumesi = set()

        for i in self.sade_kelimeler:

            kelimeler_kumesi.add(i)
        print("Tum kelimeler")
        for i in kelimeler_kumesi:
            print(i)
            print("***********************")
    def kelime_frekansi(self):

        kelime_sozluk = dict()

        for i in self.sade_kelimeler:

            if (i in kelime_sozluk):

                kelime_sozluk[i] += 1

            else:
                kelime_sozluk[i] = 1

        for kelime,sayi in kelime_sozluk.items():
            print("{} kelimesi {} defa geciyor....".format(kelime,sayi))

            print("---------------------------------")
    def kelime_sayisi_bulma(self):

        for i in self.sade_kelimeler:

            if (i in self.ucuncufonklist):

                self.ucuncufonklist[i] += 1

            else:

                self.ucuncufonklist[i] = 1
        print(self.ucuncufonklist)
        sor = input("Hangi kelimeyi ariyorsunuz: ")

        if (sor in self.ucuncufonklist):

            print("{} kelimesi var ve {} kere gecti".format(sor,self.ucuncufonklist[sor]))

        else:
            print("{} kelimesi yok".format(sor))





dosya = Dosya()

dosya.kelime_sayisi_bulma()
