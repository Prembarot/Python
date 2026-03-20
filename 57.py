# append - add values in form of array
mylist=[]
flag=0
for i in range(5):
    x=int(input("Enter number :"))
    mylist.append(x)


num=int(input("Enter nmber :"))
for val in mylist:
    if val==num:
        flag=1
        break
if flag==1:
    print("value is found")
else:
    print("not found")