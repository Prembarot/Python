x=int(input("Enter x :"))
a=0
b=1
c=a+b
print(a,end="")
print(b,end="")
while x-2>0 :
    x=x-1
    b=a
    a=c
    c=a+b
    print(c, end="")