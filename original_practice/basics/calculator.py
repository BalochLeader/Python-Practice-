
operator = input("Enter Your Operator (+ - × / ) : ")

num1 = float(input("Enter Number 1 : "))
num2 = float(input("Enter Number 2 : "))

if operator == "+":
    result = num1 + num2
    print(result)
    
elif operator == "-":
    result = num1 - num2 
    print(round(result),3)
    
elif operator == "/":
    result = num1 / num2 
    print(round(result),3)
    
    
elif operator == "×":
    result = num1 * num2 
    print(round(result),3)
    
else:
    print(" A Project Made By Diwas  ")