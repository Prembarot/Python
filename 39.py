#  wap to check whether the given number is prime or not

num=int(input("Enter number"))
flag=0  ##flag==0 means prime
for i in range(2,num):
    if num%i==0  :
        flag=1
        break
    else:
        pass

if flag==0:
    print("PRIEM NUMBER")
else:
    print("COMPOSITE NUMBER")