
import os

def generate_data_structures_programs(count, path):
    for i in range(1, count + 1):
        filename = os.path.join(path, f"data_structure_example_{i}.py")
        content = f"""# Data Structure Example {i}
# This program demonstrates basic operations with a list, tuple, set, and dictionary.

# List example
my_list = [1, 2, 3, 4, 5]
print(f"Original list: {{my_list}}")
my_list.append(6)
print(f"List after append: {{my_list}}")
my_list.remove(2)
print(f"List after remove: {{my_list}}")

# Tuple example
my_tuple = (10, 20, 30)
print(f"Original tuple: {{my_tuple}}")
print(f"Element at index 0: {{my_tuple[0]}}")

# Set example
my_set = {{'apple', 'banana', 'cherry'}}
print(f"Original set: {{my_set}}")
my_set.add('date')
print(f"Set after add: {{my_set}}")
my_set.discard('banana')
print(f"Set after discard: {{my_set}}")

# Dictionary example
my_dict = {{'name': 'Alice', 'age': 30}}
print(f"Original dictionary: {{my_dict}}")
my_dict['city'] = 'New York'
print(f"Dictionary after add: {{my_dict}}")
print(f"Alice's age: {{my_dict['age']}}")
"""
        with open(filename, 'w') as f:
            f.write(content)

def generate_algorithms_programs(count, path):
    for i in range(1, count + 1):
        filename = os.path.join(path, f"algorithm_example_{i}.py")
        content = f"""# Algorithm Example {i}
# This program demonstrates a simple sorting algorithm (Bubble Sort).

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

my_array = [64, 34, 25, 12, 22, 11, 90]
print(f"Original array: {{my_array}}")
sorted_array = bubble_sort(my_array)
print(f"Sorted array: {{sorted_array}}")
"""
        with open(filename, 'w') as f:
            f.write(content)

def generate_file_io_programs(count, path):
    for i in range(1, count + 1):
        filename = os.path.join(path, f"file_io_example_{i}.py")
        content = f"""# File I/O Example {i}
# This program demonstrates writing to and reading from a text file.

file_name = "sample_file_{i}.txt"

# Writing to a file
with open(file_name, 'w') as f:
    f.write("Hello, this is line 1.\n")
    f.write("This is line 2.\n")
print(f"Content written to {{file_name}}")

# Reading from a file
with open(file_name, 'r') as f:
    content = f.read()
print(f"Content read from {{file_name}}:\n{{content}}")
"""
        with open(filename, 'w') as f:
            f.write(content)

def generate_oop_programs(count, path):
    for i in range(1, count + 1):
        filename = os.path.join(path, f"oop_example_{i}.py")
        content = f"""# OOP Example {i}
# This program demonstrates a simple class and object creation.

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{{self.name}} says Woof!"

my_dog = Dog("Buddy", 3)
print(f"My dog's name is {{my_dog.name}} and he is {{my_dog.age}} years old.")
print(my_dog.bark())
"""
        with open(filename, 'w') as f:
            f.write(content)

def generate_web_scraping_programs(count, path):
    for i in range(1, count + 1):
        filename = os.path.join(path, f"web_scraping_example_{i}.py")
        content = f"""# Web Scraping Example {i}
# This program demonstrates a basic web scraping using requests (without BeautifulSoup for simplicity).
# Note: For real-world scraping, consider using BeautifulSoup for parsing HTML.

import requests

url = "https://www.example.com"
try:
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Successfully fetched content from {{url}}")
        # print(response.text[:500]) # Print first 500 characters of the content
    else:
        print(f"Failed to fetch content. Status code: {{response.status_code}}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {{e}}")
"""
        with open(filename, 'w') as f:
            f.write(content)

def generate_gui_programs(count, path):
    for i in range(1, count + 1):
        filename = os.path.join(path, f"gui_example_{i}.py")
        content = f"""# GUI Example {i}
# This program demonstrates a simple Tkinter GUI window.
# Note: This will open a GUI window when executed.

import tkinter as tk

def on_button_click():
    label.config(text="Hello, Tkinter!")

root = tk.Tk()
root.title("GUI Example {i}")

label = tk.Label(root, text="Click the button")
label.pack(pady=10)

button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack(pady=5)

# root.mainloop()
"""
        with open(filename, 'w') as f:
            f.write(content)

def generate_date_time_programs(count, path):
    for i in range(1, count + 1):
        filename = os.path.join(path, f"date_time_example_{i}.py")
        content = f"""# Date and Time Example {i}
# This program demonstrates basic date and time operations.

from datetime import datetime, timedelta

# Current date and time
now = datetime.now()
print(f"Current date and time: {{now}}")

# Formatting date and time
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print(f"Formatted date and time: {{formatted_date}}")

# Adding a timedelta
future_date = now + timedelta(days=7)
print(f"Date after 7 days: {{future_date}}")
"""
        with open(filename, 'w') as f:
            f.write(content)

def generate_error_handling_programs(count, path):
    for i in range(1, count + 1):
        filename = os.path.join(path, f"error_handling_example_{i}.py")
        content = f"""# Error Handling Example {i}
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

print(f"10 / 2 = {{divide(10, 2)}}")
print(f"10 / 0 = {{divide(10, 0)}}")
print(f"10 / 'a' = {{divide(10, 'a')}}")
"""
        with open(filename, 'w') as f:
            f.write(content)

def generate_regex_programs(count, path):
    for i in range(1, count + 1):
        filename = os.path.join(path, f"regex_example_{i}.py")
        content = f"""# Regular Expression Example {i}
# This program demonstrates basic regex matching.

import re

text = "The quick brown fox jumps over the lazy dog."
pattern = r"fox"

match = re.search(pattern, text)
if match:
    print(f"Pattern '{{pattern}}' found in text at position {{match.start()}}")
else:
    print(f"Pattern '{{pattern}}' not found.")

pattern_all = r"o"
matches_all = re.findall(pattern_all, text)
print(f"All occurrences of '{{pattern_all}}': {{matches_all}}")
"""
        with open(filename, 'w') as f:
            f.write(content)

def generate_networking_programs(count, path):
    for i in range(1, count + 1):
        filename = os.path.join(path, f"networking_example_{i}.py")
        content = f"""# Networking Example {i}
# This program demonstrates a simple client-side socket connection.
# Note: This requires a server to connect to. For demonstration, it will try to connect to a non-existent server.

import socket

host = 'localhost'
port = 12345

try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(f"Connected to {{host}}:{{port}}")
    client_socket.sendall(b"Hello, server!")
    data = client_socket.recv(1024)
    print(f"Received from server: {{data.decode()}}")
    client_socket.close()
except ConnectionRefusedError:
    print(f"Connection refused. Make sure a server is running on {{host}}:{{port}}")
except Exception as e:
    print(f"An error occurred: {{e}}")
"""
        with open(filename, 'w') as f:
            f.write(content)


if __name__ == "__main__":
    base_path = "/home/ubuntu/Python-Practice-/new_practice"
    num_programs_per_category = 50 # Adjust this number to get 300-700 total programs

    generate_data_structures_programs(num_programs_per_category, os.path.join(base_path, "data_structures"))
    generate_algorithms_programs(num_programs_per_category, os.path.join(base_path, "algorithms"))
    generate_file_io_programs(num_programs_per_category, os.path.join(base_path, "file_io"))
    generate_oop_programs(num_programs_per_category, os.path.join(base_path, "oop"))
    generate_web_scraping_programs(num_programs_per_category, os.path.join(base_path, "web_scraping"))
    generate_gui_programs(num_programs_per_category, os.path.join(base_path, "gui"))
    generate_date_time_programs(num_programs_per_category, os.path.join(base_path, "date_time"))
    generate_error_handling_programs(num_programs_per_category, os.path.join(base_path, "error_handling"))
    generate_regex_programs(num_programs_per_category, os.path.join(base_path, "regex"))
    generate_networking_programs(num_programs_per_category, os.path.join(base_path, "networking"))

    print(f"Generated {num_programs_per_category * 10} programs across 10 categories.")
