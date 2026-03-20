#  create a list from specified start to end index and transfer that data to anoter list 
#  NOte : start index must not be negative and end index must not be gretarer hen length of the list

list=[10,20,30,40,50,60,70,80,90,100]
print(list)

a=int(input("enter elemnt 1 :"))
b=int(input("enter elemnt 2 :"))

if a>=0 and b<=len(list): 
    list1=list[a:b]
    print("list1",list1)
else:
    print("No list found")


 