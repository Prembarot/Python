a=["prem","rdm","purvik","jay","jainam","putin","trump"]

fp= open("abc.txt","w")

for name in a:
    fp.write(name+"\n")

fp.close()

fp= open("abc.txt","r")
    
for name in fp:
    print(name)
