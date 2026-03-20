# wap to print all numbers divdible by M and N in list 

arr=[10,20,30,40,50,60,70]
M=5
N=3

for x in arr:
    if x%M==0 and x%N==0:
        print(x," Is Divisible")
    else:
        print(x,"Not Divisible")