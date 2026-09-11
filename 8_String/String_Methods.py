# Python String Methods Cheat Sheet
# A string is a sequence of characters enclosed in single quotes, double quotes, or triple quotes.
# These methods are built into Python and help us manipulate strings efficiently.

text = "hello world"

# 1. capitalize()
# Converts the first character to uppercase and the rest to lowercase.
print(text.capitalize())      # Output: Hello world

# 2. casefold()
# More aggressive version of lower() for case-insensitive comparison.
print("BETA".casefold())     # Output: beta

# 3. center(width, fillchar)
# Centers the string within a given width.
print(text.center(20, "-"))  # Output: ----hello world----

# 4. count(substring, start, end)
# Counts how many times a substring appears.
print(text.count("o"))       # Output: 2

# 5. encode(encoding='utf-8', errors='strict')
# Encodes the string into bytes using a specific encoding.
print(text.encode())          # Output: b'hello world'

# 6. endswith(suffix, start, end)
# Checks whether the string ends with the given suffix.
print(text.endswith("ld"))   # Output: True

# 7. expandtabs(tabsize=8)
# Replaces tab characters with spaces.
print("a\tbc".expandtabs(4)) # Output: 'a   bc'

# 8. find(substring, start, end)
# Returns the index of the first occurrence; returns -1 if not found.
print(text.find("w"))        # Output: 6

# 9. format(*args, **kwargs)
# Formats values inside a string using placeholders.
print("{} {}".format("Hello", "Python"))  # Output: Hello Python

# 10. format_map(mapping)
# Similar to format(), but works with a dictionary.
print("{name} is {age}".format_map({"name": "Aman", "age": 20}))

# 11. index(substring, start, end)
# Same as find() but raises ValueError if substring is not found.
print(text.index("o"))       # Output: 4

# 12. isalnum()
# Returns True if all characters are letters or digits.
print("abc123".isalnum())    # Output: True

# 13. isalpha()
# Returns True if all characters are alphabetic.
print("abc".isalpha())       # Output: True

# 14. isascii()
# Returns True if all characters are ASCII characters.
print("hello".isascii())     # Output: True

# 15. isdecimal()
# Returns True if all characters are decimal digits.
print("123".isdecimal())     # Output: True

# 16. isdigit()
# Returns True if all characters are digits.
print("123".isdigit())       # Output: True

# 17. isidentifier()
# Checks if the string is a valid Python identifier.
print("variable_1".isidentifier())  # Output: True

# 18. islower()
# Checks if all alphabetic characters are lowercase.
print("hello".islower())      # Output: True

# 19. isnumeric()
# Checks if all characters are numeric.
print("123".isnumeric())     # Output: True

# 20. isprintable()
# Returns True if all characters are printable.
print("Hello".isprintable()) # Output: True

# 21. isspace()
# Checks if the string contains only whitespace.
print("   ".isspace())      # Output: True

# 22. istitle()
# Checks if each word starts with uppercase and rest are lowercase.
print("Hello World".istitle())  # Output: True

# 23. isupper()
# Checks if all alphabetic characters are uppercase.
print("HELLO".isupper())     # Output: True

# 24. join(iterable)
# Joins elements of an iterable into a single string.
print("-".join(["a", "b", "c"]))  # Output: a-b-c

# 25. ljust(width, fillchar)
# Left-justifies the string.
print(text.ljust(20, "*"))   # Output: hello world*********

# 26. lower()
# Converts all characters to lowercase.
print("HELLO".lower())       # Output: hello

# 27. lstrip(chars)
# Removes leading characters (spaces by default).
print("   hello".lstrip())   # Output: hello

# 28. maketrans(x, y, z)
# Creates a translation table used with translate().
trans = str.maketrans({"h": "H", "o": "O"})
print("hello".translate(trans))  # Output: HeOllO

# 29. partition(separator)
# Splits the string into 3 parts: before, separator, after.
print("hello,world".partition(","))  # Output: ('hello', ',', 'world')

# 30. replace(old, new, count)
# Replaces occurrences of a substring.
print("banana".replace("a", "@"))  # Output: b@n@n@

# 31. rfind(substring, start, end)
# Finds the last occurrence of a substring.
print(text.rfind("o"))       # Output: 7

# 32. rindex(substring, start, end)
# Same as rfind() but raises ValueError if not found.
print(text.rindex("o"))      # Output: 7

# 33. rjust(width, fillchar)
# Right-justifies the string.
print(text.rjust(20, "*"))   # Output: *********hello world

# 34. rpartition(separator)
# Splits from the right side into 3 parts.
print("hello,world".rpartition(","))  # Output: ('hello', ',', 'world')

# 35. rsplit(sep=None, maxsplit=-1)
# Splits the string from the right.
print("a b c".rsplit())      # Output: ['a', 'b', 'c']

# 36. rstrip(chars)
# Removes trailing characters.
print("hello   ".rstrip())   # Output: hello

# 37. split(sep=None, maxsplit=-1)
# Splits the string into a list of substrings.
print(text.split())           # Output: ['hello', 'world']

# 38. splitlines(keepends=False)
# Splits a string at line breaks.
print("a\nb\nc".splitlines())  # Output: ['a', 'b', 'c']

# 39. startswith(prefix, start, end)
# Checks whether the string starts with the given prefix.
print(text.startswith("he")) # Output: True

# 40. strip(chars)
# Removes leading and trailing whitespace or specified characters.
print("  hello  ".strip())   # Output: hello

# 41. swapcase()
# Swaps uppercase to lowercase and vice versa.
print("HeLLo".swapcase())    # Output: hEllO

# 42. title()
# Converts each word to title case.
print("hello world".title()) # Output: Hello World

# 43. translate(table)
# Replaces characters according to a translation table.
trans = str.maketrans({"h": "H", "e": "E"})
print("hello".translate(trans))  # Output: HEllo

# 44. upper()
# Converts all characters to uppercase.
print("hello".upper())       # Output: HELLO

# 45. zfill(width)
# Pads the string on the left with zeros.
print("42".zfill(5))         # Output: 00042

# Extra notes:
# - len(string) is a built-in function, not a string method, used to get length.
# - The in operator checks if a substring exists inside a string.
# - Strings are immutable, which means methods return a new string instead of changing the original.

# Example:
name = "python"
print(len(name))              # Output: 6
print("py" in name)          # Output: True

# End of String Methods Tutorial
