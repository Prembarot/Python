# enter any number 

a=int(input("Enter a"))
sum=0
for i in range(0,a):
    print(i,"+",end=" ")
    sum=sum+i
print(a, "=", sum+a)
    
for i in range(0,a+1):
    sum=sum+i
    print(i,"->",sum)
    
