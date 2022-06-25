import time
class deneme():

    def __init__(self,isim,numara,maas,diller):
        print("Init veritabani yuklendi...")
        self.isim = isim
        self.numara = numara
        self.maas = maas
        self.diller = diller
    def bilgilerigoster(self):
        print("""
        
        isim: {}
        
        numara = {}
        
        maas = {}
        
        diller = {}
        
        """.format(self.isim,self.numara,self.maas,self.diller))

    def dil_ekle(self,yeni_dil):
        print("Dil ekleniyor...")
        time.sleep(0.5)
        self.diller.append(yeni_dil)

    def maas_ekle(self,yeni_zam):
        print("maas ekleniyor...")
        time.sleep(0.5)
        self.maas += yeni_zam

ogrenci1 = deneme("sa",12,3400,["C++","Django","Java"])

print(ogrenci1.diller)

ogrenci1.bilgilerigoster()

ogrenci1.dil_ekle("sa")

ogrenci1.maas_ekle(200)

ogrenci1.bilgilerigoster()
