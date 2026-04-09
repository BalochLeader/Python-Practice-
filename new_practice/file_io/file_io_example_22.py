# File I/O Example 22
# This program demonstrates writing to and reading from a text file.

file_name = "sample_file_22.txt"

# Writing to a file
with open(file_name, 'w') as f:
    f.write("Hello, this is line 1.
")
    f.write("This is line 2.
")
print(f"Content written to {file_name}")

# Reading from a file
with open(file_name, 'r') as f:
    content = f.read()
print(f"Content read from {file_name}:
{content}")
