##Shoping Cart Program

foods = []

prices = []

total = 0


while True:
	food = input("Enter Foods  (q to quite ) : ")
	if food.lower() == "q":
		break
		
	else:
		prices=float(input(f"Enter Your Price To These Food {food}: "))
		foods.append(food)
		prices.append(prices)
		
print("---------------Cart-----------------")
		
for food in foods:
		print(foods)	
for price in prices:
		prices =+ price 
		
print()
	
print(f"Here Is Your Food {foods} amd Price {prices} $ ")
		
	
	