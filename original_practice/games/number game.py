import random

n= random.randint(1,50)
a = 1
guess = 1
while (a!=n):
    a = int(input("Enter No : "))
    if (a>n):
       print("Lower No. Plzz ")
       guess +=1
    elif(a<n):
        print("Higher No. PlZ")
        guess +=1
        
result = input("Your Guess Is Correct Do You Want To See Result (Y/N) :")
if result == "Y":
        print(f"Your Guess Attemp : {guess}")
        print(f"Your Guess Number : {n}")
        print(f"")
        
elif result=="N":
    print("!Why ?")
    
print("--------------------------------------------")
score = input("You Need Extact Score (y/n) : ")

op = random.randint(60,80)
opp = random.randint(30,40)
if (guess==7):
    print(f"Your Score Is {op}")
    
elif (guess==10):
    print(f"Your Score Is {opp}")
    
    
print("")

