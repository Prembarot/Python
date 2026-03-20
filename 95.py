a= ["Cheese","Paneer","Dal"]
b= ["Burger","Roll","Rice"]

x=zip(a,b)

for i, (a,b) in enumerate(zip(a,b)):    ## enumerate ==> for getting numbers in front!!
    print(i+1,a,b)
    
    
### UNZIP !!
toopings , base  = zip(*x)
print("Toopings are :",toopings)
print("Base :",base)