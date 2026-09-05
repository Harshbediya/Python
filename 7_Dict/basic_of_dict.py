"""Basic dictionary properties and methods."""

# A dictionary stores data as key-value pairs.
#
# Main properties of a dictionary:
# 1. It is mutable, so values can be changed after creation.
# 2. Keys must be unique. A repeated key replaces the old value.
# 3. Keys must be hashable, such as str, int, float, or tuple.
# 4. Values can have any data type and can be repeated.
# 5. Dictionaries preserve insertion order in modern Python.
#
#  ******** Important points to remember: ************

# 6. A dictionary is written with curly brackets: {}.
# 7. Every item has the form key: value.
# 8. Keys must be unique. If a key is repeated, the latest value is kept.
# 9. Keys must be immutable/hashable, but values can be mutable.
# 10. A dictionary can contain different data types as keys and values.
# 11. An empty dictionary is written as {}, not set().
# 12. Use dict() or {} to create a dictionary.
# 13. Use dictionary[key] when the key is known and must exist.
# 14. Use get(key) when a missing key should not raise an error.
# 15. The in operator checks keys by default, not values.
# 16. len(dictionary) returns the number of key-value pairs.
# 17. clear() removes all items, while del removes a selected item.
# 18. Dictionary keys and values can be viewed with keys(), values(), and
#     items().


# ------------------------- Creating a dictionary -------------------------
student = {
	"name": "Aman",
	"age": 20,
	"course": "Python",
}

print("Original dictionary:", student)

# Read a value with its key. A missing key raises KeyError.
print("Student name:", student["name"])

# get() reads a value safely and returns None, or another default value,
# when the key does not exist.
print("City:", student.get("city"))
print("City with default:", student.get("city", "Not available"))


# --------------------------- Adding and changing -------------------------
student["city"] = "Delhi"       # Add a new key-value pair.
student["age"] = 21             # Change an existing value.
student.update({"grade": "A", "age": 22})  # Add or change many values.
print("After adding and updating:", student)


# ------------------------------- Dictionary methods ----------------------
# keys() returns a view containing all keys.
print("Keys:", student.keys())

# values() returns a view containing all values.
print("Values:", student.values())

# items() returns a view of (key, value) pairs.
print("Items:", student.items())

# Loop through keys and values.
for key, value in student.items():
	print(key, "=", value)

# setdefault() returns the value if the key exists. Otherwise, it adds the
# key with the supplied default value.
student.setdefault("country", "India")
print("After setdefault:", student)

# pop() removes a key and returns its value.
removed_grade = student.pop("grade")
print("Removed grade:", removed_grade)

# popitem() removes and returns the last inserted key-value pair.
last_item = student.popitem()
print("Removed last item:", last_item)

# copy() creates a shallow copy of the dictionary.
student_copy = student.copy()
print("Copied dictionary:", student_copy)

# Membership checks keys, not values.
print("name" in student)       # True
print("Aman" in student)       # False

# len() returns the number of key-value pairs.
print("Number of pairs:", len(student))

# del removes one key-value pair.
del student["city"]
print("After del:", student)

# clear() removes every item from the dictionary.
student.clear()
print("After clear:", student)


# fromkeys() creates a dictionary from a sequence of keys.
subjects = dict.fromkeys(["math", "english", "science"], 0)
print("Subjects:", subjects)
