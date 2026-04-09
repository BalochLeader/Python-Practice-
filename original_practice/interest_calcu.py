
#Simple Intrest Calculator Using Python 


principle = 0
time = 0
rate = 0

while principle <= 0:
    principle = float(input("Enter Principle : "))
    if principle <= 0:
        print("Principle Cannot Be Negative")

while time <= 0:
    time = float(input("Enter Time : "))
    if time <= 0:
        print("Time Cannot Be Negative ")
        
while rate <= 0:
    rate = float(input("Enter Rate Of Intrest : "))
    if rate <= 0:
        rate = input("Rate Of Intrest Cannot Be Negative ")
      
      
      
result = principle * ( time * rate/ 100 )

print(f"Your Intrest At The {time} Years After ${result: .2f} ")

print("Thanks For Using These Calculator")