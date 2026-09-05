
"""
Python Lists
============

A list stores multiple values in one variable.
Lists are:
- Ordered
- Mutable (changeable)
- Allow duplicate values
- Can contain different data types
"""

# Creating lists
numbers = [10, 20, 30, 40]
names = ["Alice", "Bob", "Charlie"]
mixed = [1, "Python", 3.14, True]
empty_list = []

# Accessing items (index starts at 0)
print(numbers[0])       # 10
print(numbers[-1])      # 40

# Slicing
print(numbers[1:3])     # [20, 30]
print(numbers[:2])      # First two items
print(numbers[::2])     # Every second item

# Changing items
numbers[0] = 100
print(numbers)

# Adding items
numbers.append(50)             # Add one item at the end
numbers.insert(1, 15)          # Add item at a specific index
numbers.extend([60, 70])       # Add multiple items

# Removing items
numbers.remove(15)             # Remove the first matching value
last_item = numbers.pop()      # Remove and return the last item
numbers.pop(0)                 # Remove item at index 0
# del numbers[0]               # Delete item by index
# numbers.clear()              # Remove all items

# Useful operations
print(len(numbers))            # Number of items
print(20 in numbers)           # Check whether an item exists
print(numbers + [80, 90])      # Join lists
print(numbers * 2)             # Repeat a list

# Sorting and reversing
numbers.sort()                 # Sort in ascending order
numbers.sort(reverse=True)     # Sort in descending order
numbers.reverse()              # Reverse the current order

# Copying a list
copy_list = numbers.copy()
another_copy = list(numbers)

# Looping through a list
for item in names:
    print(item)

for index, item in enumerate(names):
    print(index, item)

# List comprehension
squares = [number ** 2 for number in range(1, 6)]
print(squares)

# Built-in list methods
"""
append(item)              Add an item at the end
clear()                   Remove all items
copy()                    Return a shallow copy
count(item)               Count occurrences of an item
extend(iterable)          Add multiple items
index(item)               Return the index of the first matching item
insert(index, item)       Insert an item at a position
pop(index=-1)             Remove and return an item
remove(item)              Remove the first matching item
reverse()                 Reverse the list
sort()                    Sort the list
"""

# Examples of methods
values = [3, 1, 2, 1]

values.append(4)
print(values.count(1))     # 2
print(values.index(2))     # 2

values.sort()
print(values)

values.reverse()
print(values)

# Important points
"""
1. Indexing starts from 0.
2. Negative indexes access items from the end.
3. Lists are mutable, so their items can be changed.
4. Lists allow duplicate values.
5. A list can contain different data types.
6. list[index] raises IndexError if the index does not exist.
7. remove(value) raises ValueError if the value is not found.
8. sort() changes the original list.
9. sorted(list) returns a new sorted list.
10. copy() should be used when an independent list is needed.
"""

# sorted() creates a new list
data = [5, 2, 8, 1]
sorted_data = sorted(data)

print(data)         # Original list remains unchanged
print(sorted_data)  # Sorted copy
