"""Examples of Python's numeric string-checking methods."""

# isdecimal() accepts decimal digits commonly used to write base-10 numbers.
print("123".isdecimal())  # True
print("²".isdecimal())    # False: a superscript digit is not decimal

# isdigit() also accepts digit characters such as superscript digits.
print("123".isdigit())   # True
print("²".isdigit())     # True

# isnumeric() is the broadest check; it also accepts numeric characters
# such as fractions.
print("123".isnumeric())  # True
print("²".isnumeric())    # True
print("½".isnumeric())    # True

# Each method returns True only when the string is non-empty and every
# character passes that method's check.
print("12.3".isnumeric())  # False: the decimal point is not numeric
print("".isnumeric())     # False: an empty string has no numeric characters
