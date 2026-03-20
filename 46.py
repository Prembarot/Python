# 1 1 1 1 15
# 2 2 2 2 2
# 3 3 3 3 3
# 4 4 4 4 4 
# 5 5 5 5 5
#  Pattern

a=int(input("Enter a"))
for i in range(1,a+1):
    for j in range(a):
        print(i,end=" ")
    print(" ")