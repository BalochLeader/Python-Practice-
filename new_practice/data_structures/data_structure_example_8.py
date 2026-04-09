# Data Structure Example 8
# This program demonstrates basic operations with a list, tuple, set, and dictionary.

# List example
my_list = [1, 2, 3, 4, 5]
print(f"Original list: {my_list}")
my_list.append(6)
print(f"List after append: {my_list}")
my_list.remove(2)
print(f"List after remove: {my_list}")

# Tuple example
my_tuple = (10, 20, 30)
print(f"Original tuple: {my_tuple}")
print(f"Element at index 0: {my_tuple[0]}")

# Set example
my_set = {'apple', 'banana', 'cherry'}
print(f"Original set: {my_set}")
my_set.add('date')
print(f"Set after add: {my_set}")
my_set.discard('banana')
print(f"Set after discard: {my_set}")

# Dictionary example
my_dict = {'name': 'Alice', 'age': 30}
print(f"Original dictionary: {my_dict}")
my_dict['city'] = 'New York'
print(f"Dictionary after add: {my_dict}")
print(f"Alice's age: {my_dict['age']}")
