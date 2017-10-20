def z0(a,n):
    for i in range(n-1):
        a[n-(i+2)],a[n-(i+1)]=a[n-(i+1)],a[n-(i+2)]
    return(a)
print("задайте массив")
a=list(input().split())
n=len(a)
print("исходный массив - ",a)
k=int(input("задайте кол-во сдвигов массива - "))
for i in range(k):
    a=z0(a,n)
print("сдвинутый массив",a)
