import os
from datetime import datetime

listtxt = list()

listpdf = list()

listmp4 = list()

t = os.getcwd()
for i,s,d  in os.walk(t):

    print(i)
    print(s)
    print(d)


    for x in d:

        print(x)


with open("mp4_ile_bitenler.txt", "w", encoding="utf-8") as mp4:
         for l in listmp4:
             mp4.write(l)
             mp4.write("\n")

with open("txt_ile_bitenler.txt","w",encoding="utf-8") as txt:
    for l in listtxt:
        txt.write(l)
        txt.write("\n")

with open("pdf_ile_bitenler.txt", "w", encoding="utf-8") as pdf:
    for l in listpdf:
        pdf.write(l)
        pdf.write("\n")




