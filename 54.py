# ARRAY- also known as list in python

arr= [200,300,400,500]
c=0
sum=0
# print(arr)

for val in arr:
    val=val+50
    c=c+1
    sum=val+sum
    print("value of array :",val)
print("Total count: ",c)
print(sum)
