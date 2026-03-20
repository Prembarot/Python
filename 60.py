#  wap to find max and min value from list also ask user to i/p value at run time 


mylist=[]
n=int(input("Enter number of elements :"))
for i in range(n):
    x=int(input("Enter number :"))
    mylist.append(x)
print(mylist)

max=mylist[0]
min=mylist[0]

for i in mylist:
    if x>max:
        max=x
        
    if x<min:
        min=x
        
print("max :",max)
print("min :",min)