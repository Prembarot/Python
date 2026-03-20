price = [30,10,25,15,0]
item = ["Franky", "Dabel1", "Samosa", "Panipuri", "Khichdi"] 
food = zip(price, item)

# money, food = zip(*sorted (zip(price, item)))
# print("Money = ", money)
# print("Food =", food)

money, food = zip(*sorted(zip(item, price)))
print("Money = ",money)
print("Food = ",food)