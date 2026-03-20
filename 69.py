## DICTIONARY

## DICTIONARY=(key,value) pair 
company={
    "id" : 101,       #key : value 
    "name" : "compact",
    "assests " : 1000000
}

# print(company)

print(company['id'],",",company['name'],",",company['assests '])


# DICTIONARY with looping

print("key  value")
for key,value in company.items() :
    print(key," => ",value)
    
    
#  Conditions

if "name" in company:
    print("Name of comapny : ",company['name'])
else:
    print("not exist")