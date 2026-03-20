# reverse number 
a=123
rev=0

while(a>0):
    rem= a%10      #remainder
    rev = rev*10+rem
    a=int(a/10  )   ##quotient
print("reversed number : ",rev)
