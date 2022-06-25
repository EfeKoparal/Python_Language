"""
Problem 1
Elinizde uzunca bir string olsun.

            "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"


Bu strling içindeki harflerin frekansını (bir harfin kaç defa geçtiği) bumaya çalışın.

İpucu : Kodlama egzersizimizde buna çok benzer bir şey yapmıştık.

"""

ah = "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"

def harf_frekans (x):

    sozluk = dict()

    for i in x:
        if (i in sozluk):

            sozluk[i] += 1

        else:

            sozluk[i] = 1
    print(sozluk.items())
    return sozluk.items()

for i,j in harf_frekans(ah):

    print(i,j)

      
