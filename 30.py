#  wap to input range of numbers and print all even numbers 

a=int(input("Enter First Number: "))
b=int(input("Enter Last Number: "))
x=a
c=0
while x<=b:
    if x%2!=0:
        print("Odd:",x)
        c+=1
    x+=1
print("Count of odd numbers:",c)