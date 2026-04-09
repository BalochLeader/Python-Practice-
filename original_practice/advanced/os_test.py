import os

# 1️⃣ Current working directory
print("Current Folder:", os.getcwd())

# 2️⃣ List files/folders in current directory
print("Files here:", os.listdir())

# 3️⃣ Create a new folder
os.mkdir("MyFolder")  # creates folder named MyFolder

# 4️⃣ Rename folder
os.rename("MyFolder", "NewFolder")

# 5️⃣ Delete folder
os.rmdir("NewFolder")  # folder must be empty

# 6️⃣ Check if a file/folder exists
print("Does test.txt exist?", os.path.exists("test.txt"))

# 7️⃣ Get absolute path of a file
print("Full path:", os.path.abspath("test.txt"))