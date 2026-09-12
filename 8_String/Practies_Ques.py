"""Simple string practice questions."""

# 1. Take a name as input and print it.
#

# 2. Take a name as input and print its length.
#
# 3. Take a word as input and print it in uppercase.
#
# 4. Take a word as input and print it in lowercase.
#
# 5. Take a sentence as input and count how many spaces it has.
#
# 6. Take a string as input and print its first character.
#
# 7. Take a string as input and print its last character.
#
# 8. Take a word as input and check whether it starts with the letter "a".
#
# 9. Take a sentence as input and replace every space with a hyphen.
#
# 10. Take a word as input and check whether it is a palindrome.


# Answers

# 1. Print a name.
name = input("Enter your name: ")
print(name)

# 2. Print the length of a name.
name = input("Enter your name: ")
print(len(name))

# 3. Convert a word to uppercase.
word = input("Enter a word: ")
print(word.upper())

# 4. Convert a word to lowercase.
word = input("Enter a word: ")
print(word.lower())

# 5. Count spaces in a sentence.
sentence = input("Enter a sentence: ")
print(sentence.count(" "))

# 6. Print the first character.
text = input("Enter a string: ")
print(text[0])

# 7. Print the last character.
text = input("Enter a string: ")
print(text[-1])

# 8. Check whether a word starts with "a".
word = input("Enter a word: ")
if word.lower().startswith("a"):
	print("The word starts with a.")
else:
	print("The word does not start with a.")

# 9. Replace spaces with hyphens.
sentence = input("Enter a sentence: ")
print(sentence.replace(" ", "-"))

# 10. Check whether a word is a palindrome.
word = input("Enter a word: ")
if word.lower() == word.lower()[::-1]:
	print("It is a palindrome.")
else:
	print("It is not a palindrome.")
