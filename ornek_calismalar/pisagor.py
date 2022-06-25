"""
pisagor ucgeni bulma

c =(a**2 + b**2)**0.5

"""

def pisagor():
    liste = list()

    for a in range(1,101):
        for b in range(1, 101):
            c = (a ** 2 + b ** 2) ** 0.5
            if (c == int(c)):
                liste.append((a,b,int(c)))
    return liste
print(pisagor())
