# east way to find the number in array just like practical 57

mylist=[]
for i in range(5):
    x=int(input("Enter number :"))
    mylist.append(x)


num=int(input("Enter nmber :"))

if num in mylist:
    print("value is found")
else:
    print("not found")