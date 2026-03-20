#

from os import path

fna=input("Enter file name :")

if path.exists(fna):
    fp=open(fna,"r")
    
    for line in fp:
        print(line,end="")
else:
    print("File not found....")
    