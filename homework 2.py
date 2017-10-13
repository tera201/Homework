
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

def z3():
    def soch(a,b):
        import math
        return(math.factorial(a)/(math.factorial(b)*math.factorial(a-b)))
    n=int(input("введите число "))
    for i in range(n+1):
        for j in range(i+1):
            print(int(soch(i,j)),end=" ")
        print()
