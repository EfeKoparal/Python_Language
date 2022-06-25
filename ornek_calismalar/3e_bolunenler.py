liste = list(range(1,100))

for i in liste:

    if i % 3 != 0:
        continue
    elif i % 3 == 0:
        print(str(i) + " uce bolunur")


