class kuvvet3():

    def __init__(self,max=0):

        self.max = max

        self.kuvvet = 0

    def __iter__(self):

        return self

    def __next__(self):

        if self.kuvvet <= self.max:
            sonuc = 3 ** self.kuvvet
            self.kuvvet += 1

            return sonuc
        else:
            self.kuvvet = 0
            raise StopIteration

Kuvvet = kuvvet3(6)

for i in Kuvvet:
    print(i)

for a in Kuvvet:
    print(a)
