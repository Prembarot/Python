a= ["Cheese","Paneer","Dal"]
b= ["Burger","Roll","Rice"]

x=zip(a,b)
# print(set(x))
# print(list(x))

# for a,b in zip(a,b):
#     print(a,b)

for i, (a,b) in enumerate(zip(a,b)):
    print(i+1,a,b)