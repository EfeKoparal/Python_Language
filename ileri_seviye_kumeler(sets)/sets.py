"""
İleri Seviye Kümeler (Sets)
Bu konuda yeni bir veritipi olan kümeler veya ingilizce adıyla setleri öğreneceğiz.

Kümeler, matematikte olduğu gibi bir elemandan sadece bir adet tutan bir veritipidir. Bu açıdan kullanıldıkları yerlerde çok önemli bir veritipi olmaktadırlar. İsterseniz hemen bir küme oluşturalım.

Küme oluşturmak
x =  set() # Boş küme
type(x)
set
liste = [1,2,3,3,1,1,2,2,2] # Aynı elemanı birçok defa  barındıran bir liste
x = set(liste) # Veri tipi dönüşümü
x # Aynı elemanlar tek bir elemana indirgendi.
{1, 2, 3}
x = set("Python Programlama Dili")  # Aynı karakterler tek bir karaktere indirgendi.
x
{' ', 'D', 'P', 'a', 'g', 'h', 'i', 'l', 'm', 'n', 'o', 'r', 't', 'y'}
x = {"Python","Php","Python"}
x # Aynı elemanlar teke indirgendi.
{'Php', 'Python'}
For döngüsüyle Gezinmek
Kümeler de tıpkı sözlükler gibi sırasız bir veri tipidir. Bunu for döngüsüyle görebiliriz.

x = {"Python","Php","Java","C","Javascript"}
for i in x:
    print(i) 
Php
Python
Java
Javascript
C
Peki bir kümenin elemanlarına direk olarak ulaşabiliyor muyuz ?

x
{'C', 'Java', 'Javascript', 'Php', 'Python'}
x[0]
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
C:\Users\ORRRRR~1\AppData\Local\Temp/ipykernel_12468/3629782281.py in <module>
----> 1 x[0]

TypeError: 'set' object is not subscriptable

x["Python"]
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
C:\Users\ORRRRR~1\AppData\Local\Temp/ipykernel_12468/949411441.py in <module>
----> 1 x["Python"]

TypeError: 'set' object is not subscriptable
kumeye ulasamiyoruz...
liste = list({1,2,3,4,5})

liste[0]
"""
