def cift_mi(x):

    if x % 2 ==0 :

        return x
    else:
        raise ValueError(x,"tektir")


liste = [34,2,1,3,33,100,61,1800]


for i in liste:
    try:

        print(cift_mi(i))

    except ValueError:

        pass


