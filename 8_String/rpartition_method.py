

# Example 1: split at the last "python" in the string
s = "python is very easy and python is powerful"
print(s.rpartition("python"))
# Output: ('python is very easy and ', 'python', ' is powerful')

# Example 2: split at the last "py" in "python"
s1 = "python"
print(s1.rpartition("py"))
# Output: ('', 'py', 'thon')

# Example 3: compare with partition()
s2 = "python"
print(s2.partition("py"))
# Output: ('', 'py', 'thon')


text = "apple,banana,grape"

# left split
print(text.partition(","))   # ('apple', ',', 'banana,grape')

# right split
print(text.rpartition(",")) # ('apple,banana', ',', 'grape')



# path = "C:/Users/Alice/Documents/report.txt"

# folder, sep, file = path.rpartition("/")   
# print("Folder:", folder)
# print("Separator:", sep)
# print("File:", file)

# Folder: C:/Users/Alice/Documents
# Separator: /
# File: report.txt