price = [10000,2300,4500,2000,4000]
item= ["Jordan","Socks","Slides","Hoddie","TrackPant"]

food=zip(price,item)
# print(list(food))

# for i, (a,b) in enumerate(zip(price,item)):   
#     print(i+1,a,b)


#  UNZIP
price,food  =zip(*food)
print("Price  are :",price)
print("Items :",food)