# Shopping Cart Program

foods = []
prices = []
total = 0

while True:
    food = input("Enter food (or 'q' to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price for {food}: "))
        foods.append(food)
        prices.append(price)

print("---------------Cart-----------------")

# Print each food with its price
for i in range(len(foods)):
    print(f"{foods[i]} - ${prices[i]:.2f}")
    total += prices[i]

print("-------------------------------")
print(f"Total Price: ${total:.2f}")