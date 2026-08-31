"""
==========================================
PYTHON SETS - COMPREHENSIVE GUIDE
==========================================
A set is an unordered, mutable collection of unique elements.
"""

# ============================================
# 1. WHAT IS A SET?
# ============================================
"""
- Unordered: Elements have no specific order (index-based access not possible)
- Mutable: Can be modified after creation (add/remove elements)
- Unique: No duplicate elements allowed (automatically removes duplicates)
- Unindexed: Cannot access elements by index like lists
- No key-value pairs: Unlike dictionaries, sets only store values
"""

# ============================================
# 2. CREATING SETS
# ============================================

# Method 1: Using curly braces {}
set1 = {1, 2, 3, 4, 5}
print("Set 1:", set1)  # Output: {1, 2, 3, 4, 5}

# Method 2: Using set() constructor
set2 = set([10, 20, 30, 40])
print("Set 2:", set2)  # Output: {10, 20, 30, 40}

# Method 3: Empty set (MUST use set(), not {} which creates empty dictionary)
empty_set = set()  # Correct way
print("Empty Set:", empty_set)  # Output: set()

# NOT THIS:
not_a_set = {}  # This creates an empty dictionary, NOT a set
print("This is a dict:", type(not_a_set))  # Output: <class 'dict'>

# Method 4: Creating set from string
string_set = set("hello")
print("Set from string:", string_set)  # Output: {'h', 'e', 'l', 'o'}
# Note: Duplicates are automatically removed ('l' appears once)

# ============================================
# 3. AUTOMATIC DUPLICATE REMOVAL
# ============================================
"""
Sets automatically remove duplicate elements.
This is one of the most important properties of sets.
"""

set_with_duplicates = {1, 2, 2, 3, 3, 3, 4, 4, 4, 4}
print("Set with duplicates:", set_with_duplicates)  # Output: {1, 2, 3, 4}
# Notice: Duplicates are removed automatically

# ============================================
# 4. SET PROPERTIES
# ============================================

# Property 1: Sets are MUTABLE (can be changed)
s1 = {1, 2, 3}
s1.add(4)  # Can add elements
print("After adding 4:", s1)  # Output: {1, 2, 3, 4}

# Property 2: Sets are UNORDERED
# Elements don't have a fixed position
s2 = {5, 1, 3, 2, 4}
print("Set s2:", s2)  # Output may vary: {1, 2, 3, 4, 5} or any order

# Property 3: Sets are UNINDEXED
# Cannot access elements by index
my_set = {10, 20, 30, 40}
# print(my_set[0])  # ERROR! Sets don't support indexing

# Property 4: Only UNIQUE elements
# Duplicate values are ignored
numbers = {1, 1, 1, 2, 2, 3}
print("Unique numbers:", numbers)  # Output: {1, 2, 3}

# Property 5: Elements must be IMMUTABLE (Hashable)
valid_set = {1, 2.5, "string", (1, 2)}  # Integers, floats, strings, tuples - OK

# This would cause ERROR (lists and dicts are mutable, can't be in sets):
# invalid_set = {1, 2, [3, 4]}  # ERROR! Lists are mutable
# invalid_set = {1, 2, {3: 4}}  # ERROR! Dictionaries are mutable

# ============================================
# 5. SET METHODS - ADDING ELEMENTS
# ============================================

print("\n--- ADDING ELEMENTS ---")

# add() - Add single element
s = {1, 2, 3}
s.add(4)
print("After add(4):", s)  # Output: {1, 2, 3, 4}

# add() with duplicate (nothing happens)
s.add(2)  # 2 already exists, so nothing changes
print("After add(2):", s)  # Output: {1, 2, 3, 4} (no change)

# update() - Add multiple elements at once
s = {1, 2, 3}
s.update([4, 5, 6])
print("After update([4, 5, 6]):", s)  # Output: {1, 2, 3, 4, 5, 6}

# update() with string (adds each character)
s = {'a'}
s.update("bcd")
print("After update('bcd'):", s)  # Output: {'a', 'b', 'c', 'd'}

# ============================================
# 6. SET METHODS - REMOVING ELEMENTS
# ============================================

print("\n--- REMOVING ELEMENTS ---")

# remove() - Remove specific element (ERROR if not found)
s = {1, 2, 3, 4, 5}
s.remove(3)
print("After remove(3):", s)  # Output: {1, 2, 4, 5}

# remove() with non-existent element causes KeyError
# s.remove(10)  # ERROR! KeyError: 10

# discard() - Remove element without error if not found
s = {1, 2, 3, 4, 5}
s.discard(3)
print("After discard(3):", s)  # Output: {1, 2, 4, 5}

s.discard(10)  # No error, even though 10 doesn't exist
print("After discard(10):", s)  # Output: {1, 2, 4, 5} (unchanged)

# pop() - Remove and return arbitrary element
s = {1, 2, 3, 4, 5}
removed = s.pop()
print("Removed element:", removed)  # Output: some element from the set
print("Set after pop():", s)  # Output: 4 elements

# clear() - Remove all elements
s = {1, 2, 3}
s.clear()
print("After clear():", s)  # Output: set()

# ============================================
# 7. SET METHODS - CHECKING ELEMENTS
# ============================================

print("\n--- CHECKING ELEMENTS ---")

# in - Check if element exists
s = {1, 2, 3, 4, 5}
print("2 in set:", 2 in s)  # Output: True
print("10 in set:", 10 in s)  # Output: False

# not in - Check if element doesn't exist
print("10 not in set:", 10 not in s)  # Output: True

# len() - Get number of elements
s = {1, 2, 3, 4, 5}
print("Length of set:", len(s))  # Output: 5

# ============================================
# 8. SET OPERATIONS - MATHEMATICAL
# ============================================

print("\n--- SET OPERATIONS ---")

set_a = {1, 2, 3, 4, 5}
set_b = {3, 4, 5, 6, 7}

# Union (|) - All elements from both sets
union = set_a | set_b
print("Union (a | b):", union)  # Output: {1, 2, 3, 4, 5, 6, 7}

# Also using union() method
union2 = set_a.union(set_b)
print("Union method:", union2)  # Output: {1, 2, 3, 4, 5, 6, 7}

# Intersection (&) - Common elements in both sets
intersection = set_a & set_b
print("Intersection (a & b):", intersection)  # Output: {3, 4, 5}

# Also using intersection() method
intersection2 = set_a.intersection(set_b)
print("Intersection method:", intersection2)  # Output: {3, 4, 5}

# Difference (-) - Elements in first set but not in second
difference = set_a - set_b
print("Difference (a - b):", difference)  # Output: {1, 2}

# Also using difference() method
difference2 = set_a.difference(set_b)
print("Difference method:", difference2)  # Output: {1, 2}

# Symmetric Difference (^) - Elements in either set but not in both
sym_diff = set_a ^ set_b
print("Symmetric Difference (a ^ b):", sym_diff)  # Output: {1, 2, 6, 7}

# Also using symmetric_difference() method
sym_diff2 = set_a.symmetric_difference(set_b)
print("Symmetric Difference method:", sym_diff2)  # Output: {1, 2, 6, 7}

# ============================================
# 9. SET COMPARISON METHODS
# ============================================

print("\n--- SET COMPARISONS ---")

set_x = {1, 2, 3}
set_y = {1, 2, 3, 4, 5}
set_z = {1, 2}

# issubset() - Check if all elements of first set are in second
print("Is {1,2,3} subset of {1,2,3,4,5}?", set_x.issubset(set_y))  # True
print("Is {1,2,3} subset of {1,2}?", set_x.issubset(set_z))  # False

# Operator for subset: <=
print("Is {1,2,3} <= {1,2,3,4,5}?", set_x <= set_y)  # True

# issuperset() - Check if first set contains all elements of second
print("Is {1,2,3,4,5} superset of {1,2,3}?", set_y.issuperset(set_x))  # True
print("Is {1,2} superset of {1,2,3}?", set_z.issuperset(set_x))  # False

# Operator for superset: >=
print("Is {1,2,3,4,5} >= {1,2,3}?", set_y >= set_x)  # True

# isdisjoint() - Check if sets have NO common elements
set_p = {1, 2, 3}
set_q = {4, 5, 6}
set_r = {3, 4, 5}

print("Is {1,2,3} disjoint with {4,5,6}?", set_p.isdisjoint(set_q))  # True
print("Is {1,2,3} disjoint with {3,4,5}?", set_p.isdisjoint(set_r))  # False

# ============================================
# 10. ITERATING THROUGH SETS
# ============================================

print("\n--- ITERATING THROUGH SETS ---")

my_set = {'a', 'b', 'c', 'd'}

# Using for loop
print("Elements in set:")
for element in my_set:
    print(element)
# Note: Order may vary since sets are unordered

# ============================================
# 11. CONVERTING BETWEEN DATA TYPES
# ============================================

print("\n--- CONVERTING BETWEEN DATA TYPES ---")

# List to Set
list_data = [1, 2, 2, 3, 3, 3, 4]
set_from_list = set(list_data)
print("List:", list_data)  # [1, 2, 2, 3, 3, 3, 4]
print("Set from list:", set_from_list)  # {1, 2, 3, 4}

# Set to List
my_set = {5, 2, 8, 1}
list_from_set = list(my_set)
print("Set:", my_set)
print("List from set:", list_from_set)  # Order may vary

# Set to Tuple
my_set = {10, 20, 30}
tuple_from_set = tuple(my_set)
print("Tuple from set:", tuple_from_set)  # Order may vary

# ============================================
# 12. PRACTICAL EXAMPLES
# ============================================

print("\n--- PRACTICAL EXAMPLES ---")

# Example 1: Remove duplicates from a list
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique_numbers = list(set(numbers))
print("Remove duplicates:", unique_numbers)  # [1, 2, 3, 4] (order may vary)

# Example 2: Find common elements between two lists
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
common = set(list1) & set(list2)
print("Common elements:", common)  # {3, 4, 5}

# Example 3: Find unique elements in first list
unique_in_list1 = set(list1) - set(list2)
print("Unique to list1:", unique_in_list1)  # {1, 2}

# Example 4: Check if student is in class
class_a = {'Alice', 'Bob', 'Charlie', 'David'}
class_b = {'Bob', 'David', 'Eve', 'Frank'}

students_in_both = class_a & class_b
print("Students in both classes:", students_in_both)  # {'Bob', 'David'}

students_only_in_a = class_a - class_b
print("Only in class A:", students_only_in_a)  # {'Alice', 'Charlie'}

# ============================================
# 13. IMPORTANT NOTES & TIPS
# ============================================

"""
✓ KEY POINTS TO REMEMBER:

1. Sets CANNOT contain duplicates - they're automatically removed
2. Sets are MUTABLE - you can add/remove elements after creation
3. Sets are UNORDERED - no guaranteed element order
4. Sets are UNINDEXED - you cannot use s[0] to access elements
5. Elements must be IMMUTABLE (hashable) - no lists, dicts, or sets inside sets
6. Empty set must be created with set(), not {}
7. Useful for: removing duplicates, checking membership, mathematical operations
8. Sets are faster for membership checking than lists (use 'in' operator)
9. Set operations (union, intersection, etc.) are very efficient

✓ WHEN TO USE SETS:
- You need unique elements
- You need to check membership frequently
- You need mathematical operations (union, intersection)
- You want to remove duplicates from a list

✓ COMMON MISTAKES:
- Using {} for empty set (creates dict, not set)
- Trying to add mutable objects like lists or dicts
- Assuming sets maintain order (they don't)
- Using remove() when element might not exist (use discard() instead)
"""

# ============================================
# 14. QUICK REFERENCE TABLE
# ============================================

"""
METHOD/OPERATOR         PURPOSE                      EXAMPLE
-----------             -------                      -------
add(elem)              Add single element            s.add(5)
update(iterable)       Add multiple elements         s.update([1,2,3])
remove(elem)           Remove elem (error if not)    s.remove(5)
discard(elem)          Remove elem (no error)        s.discard(5)
pop()                  Remove & return random        s.pop()
clear()                Remove all elements           s.clear()
len(s)                 Number of elements            len(s)
elem in s              Check if element exists       5 in s
s1 | s2                Union (all from both)         s1 | s2
s1 & s2                Intersection (common)         s1 & s2
s1 - s2                Difference (in s1, not s2)    s1 - s2
s1 ^ s2                Sym Diff (in one, not both)   s1 ^ s2
s1 <= s2               Subset check                  s1 <= s2
s1 >= s2               Superset check                s1 >= s2
s1.isdisjoint(s2)      No common elements?           s1.isdisjoint(s2)
"""

print("\n✓ Sets tutorial completed!")
