print('Ali\'nin evi') # \ kacis karakteri

print("""
3 tirnakli string :)
 
sess
fsd
fds
fsdf

 
 
 
                    aaaaaa
""")


print("merhaba \tdunya") #\t tab yazar


print("merhaba\ndunya") #\n bosluk yazar

print("merhaba" + "     " + "dunya")

print("merhaba","dunya")

mesaj = "merhaba"

print(mesaj[0:6]) # anlami sudur: 0 dan 5 e kadarki karakterleri yaz. Genelde pythonda sonki karakter yazilmaz ...

print(mesaj[::2]) #ikiser ikiser karakter secti ve yazdirdi

print(mesaj[::-1]) # tersten yazdirdi

print(mesaj.upper()) # karakterleri buyuk yazdirir...

print(len(mesaj))

print(type(len(mesaj)))

print("Merhaba " * 3)

print(" {} hahahah {} ".format("31", "komik degildir")) # format kullanimi
ahmet = "ahmet"
emreden = "emreden"

daha = "daha"
print(f" {ahmet} {emreden} {daha} maldir") # fstring ... :)

