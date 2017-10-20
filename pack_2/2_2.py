def z2():
    def prof(a):
        k = a
        if a < 0:
            a = -a
        if (a != 0):
            for i in range(1, a // 2 + 1):
                if (a % i == 0):
                    k += i
        else:
            return(10)
        return(k)

    a = int(input("введите число "))
    if ((prof(a)/2)==a):
        print("число совершенное")
    else:
        print("число несовершенное")
z2()