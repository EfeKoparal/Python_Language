"""



Program 2
1'den 1000'e kadar olan sayılardan asal sayıları üreten generator bir fonksiyon yazın.


"""
import math

def asallar():

    def asalmi(x):
        asal = True
        for i in range(2,int(math.sqrt(x))+1):

            if x % i ==0:
                asal = False
        return asal
    x = 0
    while (x < 1001):
        if asalmi(x):
            yield x
        x +=1
for i in asallar():

    print(i)


