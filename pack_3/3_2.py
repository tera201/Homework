ar = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V",
             4: "IV", 1: "I"}
class tran:
    def RtoA(self,n):
        a=[]
        c=0
        for p in n:
            for i in ar:
                if ar.get(i) == p:
                    a.append(i)
        print(a)
        for i in range(len(a)):
            if i>0 and a[i]>a[i-1]:
                c+=a[i]-2*a[i-1]
            else:
                c+=a[i]
        return c
    
    def AtoR(self,n):
        a=""
        for i in ar:
            while i<=n:
                a += ar[i]
                n -= i
        return a



a=input("введите число записанное римскими цифрами ")
print(tran().RtoA(a))
b=int(input("введите число записанное арабскими цифрами "))
print(tran().AtoR(b))