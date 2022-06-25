print("""
********************
Kullanici girisi
********************


""")

sys_kullanici = "poyraz"

sys_parola = "deneme"

girishakki = 3

while True:
    if girishakki == 0:
        print("3 kere yanlis denedin siktir git")
        break

    if girishakki != 0:
        kullanici = input("kullanici adi")
        parola = input("parola")
        if (kullanici == sys_kullanici) and (parola == sys_parola) :
            print("hosgeldiniz...")
            break

        else:
            print("kullanici adi veya parola hatali")
            girishakki += -1
            print("kalan giris hakki:" + str(girishakki))



