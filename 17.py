# wap to check whwther it is a triangle is valid or not60

# total of all angle be 180 degree
#   angle should not be negatve 

a=int(input("Enter 1 angle"))
b=int(input("Enter 2 angle"))
c=int(input("Enter 3 angle"))
sum = a+b+c 
print("total angle ",sum)
if sum==180 and a>0 and b>0 and c>0 :
    print(sum,"it is triangle")
else :
    print(sum,"not triangle")