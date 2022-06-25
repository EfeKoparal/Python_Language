
x = list()
for i in range(1,1000):
    if i % 3 == 0 or i % 5 == 0:
        x.append(i)
print(x)
toplam = 0
for i in x:
    toplam += i
print(toplam)
