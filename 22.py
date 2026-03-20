# wap to input 3 numbers and find greates of three

a=int(input("Enter a :"))
b=int(input("Enter b :"))
c=int(input("Enter c :"))
if a>b and a>c :
    print("A is max ")
elif b>a and b>c :
    print("B is max ")
elif  c>a and c>b :
    print("C is max ")
else :
    print("All number are same ")