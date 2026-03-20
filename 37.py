# wap to print all odd numbers from 1 to specified number
b=int(input("Enter b :"))
sum=0
for i in range(1,b,2):
    print(i,end=" ")
    sum=sum+i
print("sum",sum)