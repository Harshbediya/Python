# A list stores multiple values in one variable.
# Lists can contain different data types and use square brackets [].
l1 = [10, 20, 3.5, "Don", 2 + 5j]
print(l1)
print(type(l1))

# Heterogeneous list: it contains different data types.
l2 = [10, 20, 3.5, "Don", 2 + 5j]
print(l2)

# Homogeneous list: all values have the same data type.
l3 = [1, 2, 3, 4]
print(l3)

# A list can contain duplicate values.
l4 = [10, 20, 30, 40, 10, 10]
print(l4)

# Indexing: the first item has index 0.
l5 = [10, "DON", 10.33]
print(l5[1])
# Negative index -1 gives the last item.
print(l5[-1])

# Slicing syntax: list[start:stop:step].
# The stop index is not included in the result.
l6 = [10, "DON", 10.33, 2 + 4j, 10, 20]
print(l6[1:4:1])

print(l6[1:4:2])
print(l6[1:3:])

# Lists are mutable, so an item can be changed after creation.
l7 = [10, 20, 30]
print(l7)
l7[0] = "iron man"
print(l7)

# Looping through a list directly gives each value one by one.
print("Values using direct looping:")
l1 = [10, 20, 30, 40, 50, 60, 70]
for value in l1:
    print(value, end=" ")
print()

# Looping with indexes: range(len(list)) creates every valid index.
print("Values using indexes:")
for index in range(len(l1)):
    print(l1[index], end=" ")
print()

# Reverse looping: start at the last index and move backwards to -1.
print("Values in reverse order:")
for index in range(len(l1) - 1, -1, -1):
    print(l1[index], end=" ")
print()
                                                          