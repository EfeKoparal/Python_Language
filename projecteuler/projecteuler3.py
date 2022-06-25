import math
number = 600851475143



def asalmi(x):
    asalmi = True
    for i in range(2,int(math.sqrt(x))+1):
        if x % i == 0:
            asalmi = False
    return asalmi

enbuyuk = 0


for i in range(2,int(math.sqrt(number)) +1):
    if number % i == 0 and asalmi(i):
        enbuyuk =i
print(enbuyuk)
