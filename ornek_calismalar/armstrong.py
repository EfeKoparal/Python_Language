a = input(
    "sayi giriniz..."
)
basamak =len(a)

tekteksayilar= list(a)

ensonkitoplam = 0

for i in tekteksayilar:
    print(i + "**" + str(basamak))
    ensonkitoplam = ensonkitoplam + (int(i)**basamak)

if ensonkitoplam == int(a):
    print("armstorng sayisidir")

else:
    print("armstrong sayisi degildir...")

