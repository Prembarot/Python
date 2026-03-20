##

from os import path

f1=input("Enter source file :")
f2=input("Enter new file :")

fs=open(f1,"r")    ## r ==> read
fd=open(f2,"w")    ## W ==> write

for line in fs:
    fd.write(line)
    
print("File copied....")
fs.close()
fd.close()
    
