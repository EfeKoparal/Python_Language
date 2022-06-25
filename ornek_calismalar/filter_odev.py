"""


Problem 2¶
Elinizden her bir elemanı 3'lü bir demet olan bir liste olsun.

     [(3,4,5),(6,8,10),(3,10,7)]

Şimdi kenar uzunluklarına göre bu kenarların bir üçgen olup olmadığını dönen bir fonksiyon yazın ve sadece üçgen belirten kenarları bulunduran listeyi ekrana yazdırın.

     [(3, 4, 5), (6, 8, 10)]




"""

def ucgenmi(x):

    if abs(x[0]-x[1])<x[2]<(x[0]+x[1]):
        return True
    else:
        return False


gonderlist = [(3,4,5),(6,8,10),(3,10,7)]

cikti = list(filter(ucgenmi,gonderlist))

print(cikti)
