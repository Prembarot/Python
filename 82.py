#  

a=int(input("Enter value of a :"))
b=int(input("Enter value of b :"))
max= lambda a,b : a if a>b else b  if b>a  else b
print("\n Max value :",max(a,b))