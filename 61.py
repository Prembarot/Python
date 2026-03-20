#  SLICING

list=[10,20,30,40,50,60]
print(list)
print("SLICED ARRAY :",list[2:4])

print(list[:4])    #firts four element
print(list[4:])    ## ele after first four
print(list[:])     # all ele

# print(list[:3])
# print(list[3:])

list1=list[:round(len(list)/2)]      # first 3
print(list1)

list2=list[round(len(list)/2):]
print(list2)

