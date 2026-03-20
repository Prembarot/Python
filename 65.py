#  Take a list of 10 elements and remove all even elemnts from list 

mylist=[210,20,30,45,53,62,71,86,91,210]
print("given list :",mylist)
a=[]
for i in mylist:
    if i%2 != 0:
      a.append(i)
mylist=a
print("ODD NUMBERS :",mylist)