"""


Bu dosyanın herbir satırını okuyun. Satırların baş harflerini birbirine ekleyerek bir string oluşturun ve bu string'i ekrana yazdırın.


"""

#dosya okuma

with open("siir.txt","r",encoding="utf-8") as kaka:
    bosliste = list()
    for i in kaka:

        i = i[:-1]

        bosliste.append(i)

print(bosliste)
kakalist = list()
for i in bosliste:
    x = i.split(" ")
    kakalist.append(x)

print(kakalist)
harfler = list()
for i in kakalist:
    harfler.append(i[0][0])
print(harfler)

for i in harfler:

    print(i,end=" ")
print("\n",end="")
for i in harfler:
    if i =="M":
        pass
    else:
        print(i)
