# ==============================================
# TUPLES IN PYTHON: BASIC NOTES AND EXAMPLES
# ==============================================

# A tuple is an ordered collection of values.
# Important points:
# 1. Tuples are ordered, so every item has a fixed index.
# 2. Tuples allow duplicate values.
# 3. Tuples can store values of different data types.
# 4. Tuples are immutable: items cannot be changed, added, or removed directly.
# 5. Tuples are written with parentheses, but the comma creates a tuple.


# -----------------------------
# 1. Creating tuples
# -----------------------------
empty_tuple = ()
numbers = (10, 20, 30, 20)
mixed_tuple = (1, "Python", 3.14, True)

# Parentheses are optional in many expressions (tuple packing).
packed_tuple = 10, 20, 30

# A one-item tuple MUST contain a trailing comma.
one_item_tuple = (10,)
not_a_tuple = (10)  # This is only an integer because there is no comma.

print("numbers:", numbers)
print("one_item_tuple:", one_item_tuple)
print("type of not_a_tuple:", type(not_a_tuple))


# -----------------------------
# 2. Accessing tuple items
# -----------------------------
print("first item:", numbers[0])       # Indexing starts at 0.
print("last item:", numbers[-1])       # -1 means the last item.
print("first three:", numbers[0:3])    # Slicing excludes the stop index.
print("every second item:", numbers[::2])
print("reversed:", numbers[::-1])


# -----------------------------
# 3. Immutability
# -----------------------------
# numbers[0] = 99
# The line above raises TypeError because tuple items cannot be reassigned.

# A tuple may contain a mutable object. The tuple itself remains immutable,
# but that inner list can be changed.
tuple_with_list = ("colors", ["red", "blue"])
tuple_with_list[1].append("green")
print("tuple containing a changed list:", tuple_with_list)


# -----------------------------
# 4. Tuple methods
# -----------------------------
print("count of 20:", numbers.count(20))
print("index of 30:", numbers.index(30))

# Tuples have only count() and index() because they cannot be modified.


# -----------------------------
# 5. Useful built-in functions
# -----------------------------
values = (4, 1, 8, 2)
print("length:", len(values))
print("smallest:", min(values))
print("largest:", max(values))
print("total:", sum(values))
print("sorted list:", sorted(values))  # sorted() returns a list.


# -----------------------------
# 6. Tuple operators and membership
# -----------------------------
print("combined:", (1, 2) + (3, 4))
print("repeated:", ("Hi",) * 3)
print("20 is present:", 20 in numbers)
print("99 is absent:", 99 not in numbers)


# -----------------------------
# 7. Packing and unpacking
# -----------------------------
# Packing: several values are grouped into one tuple.
student = "Asha", 21, "Python"

# Unpacking: tuple values are assigned to separate variables.
name, age, course = student
print(name, age, course)

# The number of variables must normally match the number of tuple items.
# Extended unpacking collects remaining values in a list.
first, *middle, last = (10, 20, 30, 40)
print("first:", first, "middle:", middle, "last:", last)

# Swap two variables without a temporary variable.
left, right = "A", "B"
left, right = right, left
print("after swap:", left, right)


# -----------------------------
# 8. Looping through a tuple
# -----------------------------
for item in numbers:
	print("item:", item)

for position, item in enumerate(numbers, start=1):
	print("position", position, "contains", item)


# -----------------------------
# 9. Nested tuples
# -----------------------------
coordinates = ((10, 20), (30, 40))
print("second point's x coordinate:", coordinates[1][0])


# -----------------------------
# 10. Converting between lists and tuples
# -----------------------------
number_list = [1, 2, 3]
number_tuple = tuple(number_list)
back_to_list = list(number_tuple)
print("list to tuple:", number_tuple)
print("tuple to list:", back_to_list)


# -----------------------------
# 11. Returning more than one value
# -----------------------------
def get_user():
	# Python returns these values together as a tuple.
	return "Ravi", 25


returned_name, returned_age = get_user()
print("returned values:", returned_name, returned_age)


# -----------------------------
# 12. Tuple or list?
# -----------------------------
# Use a tuple for fixed data that should not change, such as coordinates,
# days of the week, or a database record.
# Use a list when items need to be added, removed, or changed.

# Common mistakes:
# single = (5)     # int, not tuple
# single = (5,)    # correct one-item tuple
# numbers.append(6)  # AttributeError: tuples have no append() method
