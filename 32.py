# wap for greatest coomon divison (GCD)18
a=int(input("enter a :"))
b=int(input("enter b :"))
while a!=b :
    if a<b:
        b=b-a 
        a=a-b
        print("GCD :",a,b)
    elif a>b:
         a=a-b
         b=b-a
         print("GCD",a,b)
    else:
         print("not")        