#WAP to check weather a number is divisible by 5 and 11 or not

m = int(input("\nEnter the number"))
if (m % 5 == 0 and m % 11 ==0):
    print("it is divisible by both 5 and 11")
else :
    print("it is not divisible by both")