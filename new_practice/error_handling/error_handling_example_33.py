# Error Handling Example 33
# This program demonstrates basic try-except block for error handling.

def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero!"
    except TypeError:
        return "Error: Invalid input types!"
    else:
        return result
    finally:
        print("Division attempt finished.")

print(f"10 / 2 = {divide(10, 2)}")
print(f"10 / 0 = {divide(10, 0)}")
print(f"10 / 'a' = {divide(10, 'a')}")
