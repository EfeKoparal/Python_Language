import random
import time

class kumandacik():

    def __init__(self,tv_durum = "kapali",tv_ses = 0,kanal_listesi = ["Trt"], kanal = "Trt"):

        self.tv_durum = tv_durum
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal

    def tv_ac(self):

        if self.tv_durum == "acik":
            print("Televizyon zaten acik...")

        else:
            print("televizyon aciliyor...")
            self.tv_durum = "acik"

    def tv_kapat(self):
        if self.tv_durum == "kapali":
            print("Televizyon zaten kapali...")

        else:
            print("televizyon kapatiliyor...")
            self.tv_durum = "kapali"
    def ses_ayarlari(self):
        while True:
            cevap = input("arttir 1\nyada\nazalt 2")

            if cevap =="1":
                print("ses arttiriliyor")
                self.tv_ses +=1
            elif cevap =="2":
                self.tv_ses -=1
                print("ses kisiliyor")
            elif cevap =="q":
                print("cikiliyor")
                print(self.tv_ses)
                break
    def kanalekle(self,kanal_ismi):

         print("kanal ekleniyor...")
         time.sleep(1)

         self.kanal_listesi.append(kanal_ismi)
    def kanal_degistir(self,gitmekistediginkanal):

        print("kanal degistiriliyor")
        self.kanal = gitmekistediginkanal
        time.sleep(1)

        print('suanki kanal', gitmekistediginkanal)
    def __len__(self):
        return len(self.kanal_listesi)
    def __str__(self):
        return "Tv durumu bok gibi {} {} {} {}".format(self.kanal_listesi,self.kanal,self.tv_ses,self.tv_durum)

print("""


televizyon iste amkg

1. tv ac

2. tv kapa

3.ses ayarlari

4.kanal ekle

5.kanal sayisi

6.kanal degistir...

7. televizyon bilgileri

""")
kumandacik = kumandacik()
while True:

    islem =input("isclem seciniz ")
    if islem == "q":
        break
    elif islem == "1":
        kumandacik.tv_ac()
    elif islem == "2":
        kumandacik.tv_kapat()
    elif islem == "3":
        kumandacik.ses_ayarlari()
    elif islem == "4":
        sex = input("kanal gir")
        sexliste = sex.split(",")
        for i in sexliste:
            kumandacik.kanalekle(i)
    elif islem == "5":
        print(len(kumandacik))

    elif islem == "6":
        sex1 = input("kanal gir")
        kumandacik.kanal_degistir(sex1)
    elif islem == "7":
        print(str(kumandacik))































