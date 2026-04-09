
#while loop 

num = input("Enter Your Favourite Food  (q to quite) : ")

while not num == "q":
    print(f"{num} You Like This Food Nice")
    num = input("Enter Another Favourite Food (q to quite) : ")

print("Bye Have a Nice Day !! ")

#while loop 2 

num = int(input("Enter # Between (1,10):"))

while num < 0 or num > 10:
    print(f"{num} is Not Valid ")
    num = int(input("Try Again : Enter # Between (1,10):"))

print(f"{num} Is Your Age Wow !! ")
