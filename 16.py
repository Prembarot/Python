#  enter year and check if it is leap year or nat
year=int(input("Enter year"))
if year%4==0 :
    print(year,"Leap year")
else :
    print(year,"Not a leap year")