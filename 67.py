# 

str=input("Enter any string :")
print (str)
newstr=list(str.split(' '))

for s in newstr:
    print(s,"==>",len(s))
    