def z1():
    def rek(n):
        if (n==0):
            return(1)
        else:
            return(n*rek(n-1))

    n = int(input("рекурсивный-0 не рекурсивный-1 "))
    a = int(input("введите число "))

    import time
    c = time.time()

    if (n == 0):
        print(rek(a), " ", time.time() - c)
    else:
        for i in range(2, a + 1):
            n *= i
        print(n, " ", time.time() - c)