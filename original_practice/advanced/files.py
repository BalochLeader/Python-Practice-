#I am Writing a Simple Code 
#using Advance Python

i = int(input("Enter No : "))
def mul(i):
    for x in range(1,11):
        print(i * x)

diwas=mul(i)
#Logic 1 
#i = int(input("Enter No : "))

with open(diwas.txt , "w") as f:
        f.write(diwas)
        print("I Finally Write Your Table ")
        print(f"Your Table {i} Updated On Database ")
        