def z3():
    def soch(a,b):
        import math
        return(math.factorial(a)/(math.factorial(b)*math.factorial(a-b)))
    n=int(input("введите число строк треугольника "))
    for i in range(n):
        for k in range(n - i, 0, -1):
            print(" ", end="")
        for j in range(i+1):
            print(int(soch(i,j)),end=" ")
        print()
z3()