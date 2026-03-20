# WAP to inputa string and print words with odd length

str=input("Enter any string :")

print (str)
newstr=list(str.split(' '))

for s in newstr:
    if (len(s)%2!=0):
        print(s," => ",len(s))
      
    