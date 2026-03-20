# Write a program to check whether triangle is equilateral, scalene or isosceles
a=int(input("Enter 1st angle"))
b=int(input("Enter 2st angle"))
c=int(input("Enter 3st angle"))
if a==b==c :
    print("it is  equilateral ")
elif a==b or b==c or a==c:
    print("scalen Triangle")
else : 
    print("isosceles ")
