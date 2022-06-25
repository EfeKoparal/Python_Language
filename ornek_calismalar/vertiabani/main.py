import sqlite3

con = sqlite3.connect("kutuphane.db")

cursor = con.cursor()

def tablo_olustur():

    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık (İsim TEXT, Yazar TEXT, Yayınevi TEXT , Sayfa_Sayısı INT)")
    con.commit()

def veri_ekle():
    cursor.execute("insert into kitaplık Values('istanbul Hatirasi','amet umit','eveREST',5)")
    con.commit()
def veri_ekle2(isim,yazar,yayinevi,sayfa_sayisi):
    cursor.execute("insert into kitaplık Values(?,?,?,?)",(isim,yazar,yayinevi,sayfa_sayisi))
    con.commit()

def veri_cek():
    cursor.execute("select * from kitaplık")
    liste = cursor.fetchall()
    return liste

def veri_cek2():
    cursor.execute("select İsim,Yazar from kitaplık")
    liste = cursor.fetchall()
    print("kitaplik tablosunun bilgileri")
    for i in liste:
        print(i)
def veri_cek3(yayinevi):
    cursor.execute("select * from kitaplık where Yayınevi = ?",(yayinevi,))
    liste = cursor.fetchall()
    print("kitaplik tablosunun bilgileri")
    for i in liste:
        print(i)

def verileri_guncelle(eski_yayinevi,yeni_yayinevi):

    cursor.execute("Update kitaplık set Yayınevi= ? where Yayınevi = ?",(yeni_yayinevi,eski_yayinevi))
    con.commit()

def veri_sil (silinecek_veri):
    cursor.execute("Delete from kitaplık where Yazar = ?",(silinecek_veri,))
    con.commit()
print(veri_cek())
print("********************************")
for i in veri_cek():
    for x in i:
        print(x)
    print("********************************")

for i in veri_cek():
    print(i)
print("********************************")
print("********************************")
print("********************************")
veri_cek2() # sadece isim ve yazar aldik...
print("********************************")
print("********************************")
print("********************************")

sili = input("silinecek yazar gir\n")

veri_sil(sili)



con.close()
