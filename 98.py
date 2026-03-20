# list =[10,20,30,40,50]
# tuple=(10,20,30,40,50)
# set={10,20,30,40,50}

price = [30,10,25,15,0]
item = ["Franky", "Dabel1", "Samosa", "Panipuri", "Khichdi"] 
food = zip(price, item)

money, food = (list(t) for t in zip(*sorted(zip(item, price))))
print("Money = ",money)
print("Food = ",food)