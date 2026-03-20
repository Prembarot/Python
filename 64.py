#  wap to input elements in empty list until -1 is enter display it finf its length without using len function 
#  also ask user to enter value to remove from list and then display list 

# mylist=[]
# n=int(input("Enter number of elements :"))
# for i in range(n):
#     x=int(input("Enter number :"))
#     if (x==-1):
#         print("Loop is Stoped")
#         break
#     else:
#         mylist.append(x)
# print(mylist)

mylist=[]
print("Enter -1 to exit :")

cnt=0
while(1):
    x=int(input("Enter number :"))
    
    if (x==-1):
        print("Loop is Stoped")
        break  
    else:
         mylist.append(x)  
    cnt += 1
print(mylist)
print("Length :",cnt)

n=int(input(" Enter Element to remove :"))
mylist.remove(n)
print("removed element :",mylist)
    





