"""
"Kareler" isminde bir tane sınıf tanımlayın ve bu sınıfı iterable bir sınıf yapmaya çalışın.
Bu sınıfın init fonksiyonu maksimum isimli bir tane parametre alsın ve her next işleminde ekrana üzerinde bulunduğunuz sayının karesi yazdırılsın.
StopIteration hatası ekrana maksimum sayıyı geçtiğiniz zaman fırlatılsın.

"""


class kareler():

    def __init__(self,sayi,max):
        self.sayi = sayi
        self.max = max

        self.kuvvet = 0

    def __iter__(self):

        return self
    def __next__(self):

        if self.max >= self.kuvvet:
            sonuc =self.sayi ** self.kuvvet
            self.kuvvet += 1
            return sonuc
        else:
            raise StopIteration

kareal = kareler(5,6)

for i in kareal:
    print(i)


