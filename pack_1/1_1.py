def arifmetic(a,b,c):
    if (c == "*"):
        print(a*b)
    elif (c=="+"):
        print(a+b)
    elif (c=="-"):
        print(a-b)
    elif (c=="/"):
        if (b!=0):
            print(a/b)
        else:
            print("на 0 делить не стоит")
    else:
        return("Неизвестная операция")
arifmetic(int(input("число 1 = ")),int(input("чиcло 2 = ")),input("действие "))