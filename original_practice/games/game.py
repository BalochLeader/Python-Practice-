import random
import time

print("-------------------------------------------------")

name = input("Enter Your Name To Enter: ")

if name.strip() == "":
    print("Access Denied ❌")
    exit()
else:
    print(f"Welcome {name} 👋")

print("\nChoose Game:")
print("1 : Number Guessing Game")
print("2 : Table Game")

choice = input("Enter Your Choice: ")

def number_guessing():
    no = random.randint(1, 50)

    print("Okay Loading... Please Wait ⏳")
    time.sleep(2)

    while True:
        a = int(input("Enter Your Guess: "))

        if a == no:
            print(f"🎉 Correct! Number was {no}")
            break
        elif a > no:
            print("📉 Try Lower")
        else:
            print("📈 Try Higher")

def table_game():
    num = int(input("Enter Number for Table: "))
    print("Multiplication Table:\n")

    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

# Game selection
if choice == "1":
    number_guessing()
elif choice == "2":
    table_game()
else:
    print("Invalid Choice ❌")