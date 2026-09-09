# Basic Python string program
# Strings are text values written inside single or double quotes

# Built-in string methods in Python
# These are functions that work directly with strings

name = "Alice"
message = "Hello, welcome to Python!"

# print() shows the output on the screen
print(message)

# Access a character at a specific index (starts from 0)
print(name[0])

# Concatenation: join two strings using +
full_message = "Hello " + name + "!"
print(full_message)

# lower() converts all letters to lowercase
print(name.lower())

# upper() converts all letters to uppercase
print(name.upper())

# len() returns the length of the string
print(len(name))

# strip() removes spaces from the beginning and end
text = "   Python   "
print(text.strip())

# replace() changes one word with another
print(message.replace("Python", "Coding"))

# split() breaks a string into a list of words
words = message.split()
print(words)

# startswith() checks if the string starts with a given value
print(message.startswith("Hello"))

# endswith() checks if the string ends with a given value
print(message.endswith("!"))

# Example of string formatting
print(f"My name is {name} and I am learning Python.")

# Output:
# Hello, welcome to Python!
# A
# Hello Alice!
# alice
# ALICE
# 5
# Python
# Hello, welcome to Coding!
# ['Hello,', 'welcome', 'to', 'Python!']
# True
# True
# My name is Alice and I am learning Python.
