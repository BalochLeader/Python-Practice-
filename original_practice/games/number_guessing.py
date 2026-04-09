# Python Number Guessing Game 
import random

lowest_num = 1
highest_num = 50

answer = random.randint(lowest_num , highest_num )

gueses = 0

is_running = True 

print("Python Number Guessing Game")
print(f"Enter Any No. Between {lowest_num} and {highest_num}")
while is_running:
	guess = input("Enter Any No :  ")
	if not guess.isdigit():
		print("Broo This is Invaild ")
		continue
	guess = int(guess)
	gueses += 1 
	
	if lowest_num > guess or highest_num < guess:
		print("Out Of Range")
		print("Print No. Betwwen 1 to 50 ")
	elif guess > answer:
		print("To High Try Again")
		
	elif guess < answer:
		print("To Low Try Again")
	else:
		print(f"Correct Number You Guess Right Yippe {answer} ")
		print(f"You Guess After {gueses} Attemp W ")
		is_running = False
	
print("Thanks For Playing !! ")