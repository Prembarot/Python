# 
a=int(input("Enter a :"))
b=int(input("Enter b :"))
opr=input("Enter opr :")

def calc(a,b,opr):
    if (opr== "+"):
        return a+b 
    elif(opr=="-"):
        return a-b
    elif(opr=="*"):
        return a*b
    elif(opr=="/"):
        return a/b
    else:
        print("no apr found")    
 
print(calc(a,b,opr))
