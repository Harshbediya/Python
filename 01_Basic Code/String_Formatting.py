# String Formatting in Python
# Definition: String formatting is the process of injecting or substituting values into a string. 
# It allows you to create dynamic strings by replacing placeholders with actual values.


#                                       ******* .format() method ********

name="Harsh"
age=25
print("Hello {}".format(name))  
print("{0} is {1}".format(name, age))          # by position.
print("{n} is {a}".format(n=name, a=age))       # by keyword

#It is a method of formatting strings using the format() function. The curly braces {} act as placeholders 
# for the values that will be inserted into the string. The values are passed as arguments to the format() function, and they are inserted 
# into the string in the order they are provided.

#                                       ******* old-style string ********

# %s = string, %d = integer, %f = float, %x = hexadecimal, %o = octal, %e = scientific notation
age=25
print("Hello %s"%name) 
print("Hello, My name is %s and i am %d year old" %(name,age))
# %s is a placeholder for a string value. It is a way to format strings using the old-style string formatting syntax in Python.


#                                             ******* f-string ********  

# f-strings, also known as formatted string literals, are a way to embed expressions inside string literals, using curly braces {}.
names="Harsh"
roll_no=25
print(f"Hello {names}, roll no {roll_no}")
#  f-strings provide a concise and readable way to include variables and expressions directly within string literals.
# it allows for easier formatting and eliminates the need for explicit concatenation or the use of the format() method.
# Important: f-strings are available in Python 3.6 and later versions.

pi = 3.14159265 

print(f"{pi:.2f}")      # '3.14'         -> round to 2 decimals
print(f"{1000000:,}")   # '1,000,000'    -> comma as thousand separator
print(f"{5:03d}")       # '005'          -> pad with zeros, width 3
print(f"{0.25:.0%}")    # '25%'          -> show as percentage


pi = 3.6235    # if decimal value is upper than 5 then round up otherwise round down
print(f"{pi:.4f}")     

# How to use f-strings in Python:
# 1. Prefix the string with 'f' or 'F'.
# 2. Use curly braces {} to enclose the expressions or variables you want to include in the string.
# 3. You can include any valid Python expression inside the curly braces, including variables, function calls, and arithmetic operations.


# Notes to remember:
# - f-strings are available in Python 3.6 and later versions.
# - They provide a more readable and efficient way to format strings.
# - Expressions inside the curly braces are evaluated at runtime.