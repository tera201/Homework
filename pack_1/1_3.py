def z2():
    a = int(input("введите число "))
    k=1
    if a<0:
        a=-a
    if (a!=0):
        for i in range(1,a//2+1):
            if (a % i == 0):
                print(i)
                k += 1
                if (i == a // 2):
                    print(a)
    else:
        print("делители все числа кроме 0")
    if (k>2 or k==1):
        return('true')
    else:
        return('false')
def z3():
    if (z2()=='true'):
        print("не простое")
    else:
        print("простое")
z3()