# The original string that will be changed.
s="hello sam"
print(s)

# Define how each character should be changed.
# An empty string removes the character from the result.
d={'h':'H','l':'L','o':'@','m':''}

# str.maketrans() definition:
# It creates a translation table from the characters and their replacements.
table=str.maketrans(d)
print(table)

# str.translate() definition:
# It uses the translation table to replace or remove characters in a string.
trans=s.translate(table)
print(trans)

s1="Hello"
print(s.encode())