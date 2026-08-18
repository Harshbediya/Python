################## (+) addition #############

print(5+3)
print(5+2.4)

print(5+(3+2j))
print(5.2+(3+2j))
print((2+1j)+(3+2j))

# print(2+"World") type error  
# if you try to add a string and an integer, it will raise a TypeError because Python does not support 
# implicit type conversion between these types. You need to explicitly 
# convert the string to an integer or the integer to a string before performing the addition.
# implicit type conversion is not allowed in Python for incompatible types like string and integer.
# explicit type conversion is required to perform operations between different data types.
# example:
# a = 5
# b = "10"
# result = a + b  # This will raise a TypeError
# To fix this, you can convert the string to an integer using int() or convert
# the integer to a string using str() before performing the addition.

# ################### ( - ) subtraction ##############
print(5-3)             #2              int-int=int
print(5-2.4)           #2.6            int-float=float

print(5-(3+2j))        # (2-2j)         int-complex=complex
print(5.2-(3+2j))      # (2.2-2j)       float-complex=complex
print((2+1j)-(3+2j))   # (-1-1j)        complex-complex=complex

print(2-"World")       # TypeError: unsupported operand type(s) for -: 'int' and 'str'
print("Hello"-3.0)     # TypeError: unsupported operand type(s) for -: 'str' and 'float'
print("Hello"-(3+2j))  # TypeError: unsupported operand type(s) for -: 'str' and 'complex'
print("Hello"-"World") # TypeError: unsupported operand type(s) for -: 'str' and 'str'


####################### (*) multiplication ############

print(5*3)             #15              int+int=int
print(5*2.4)           #12.0            int+float=float

print(5*(3+2j))        # (15+10j)       int+complex=complex
print(5.2*(3+2j))      # (15.6+10.4j)   float+complex=complex
print((2+1j)*(3+2j))   # (4+7j)         complex+complex=complex


print(2*"World")       # WorldWorld    str*int=str
print("Hello"*3.0)     # TypeError: can't multiply sequence by non-int of type 'float'
print("Hello"*(3+2j))  # TypeError: can't multiply sequence by non-int of type 'complex'
print("Hello"*"World") # TypeError: can't multiply sequence by non-int of type 'str'

# ################### ( / ) division ##############
print(5/3)             #1.6666666666666667   int/int=float
print(5/2.4)          #2.0833333333333335   int/float=float

print(5/(3+2j))        # (1.1538461538461537-0.7692307692307693j)   int/complex=complex
print(5.2/(3+2j))      # (1.3846153846153846-0.9230769230769231j)   float/complex=complex
print((2+1j)/(3+2j))  # (0.6153846153846154-0.07692307692307693j)   complex/complex=complex

print(2/"World")       # TypeError: unsupported operand type(s) for /: 'int' and 'str'
print("Hello"/3.0)     # TypeError: unsupported operand type(s) for /: 'str' and 'float'
print("Hello"/(3+2j))  # TypeError: unsupported operand type(s) for /: 'str' and 'complex'
print("Hello"/"World") # TypeError: unsupported operand type(s) for /: 'str' and 'str'

# ################### ( // ) floor division ##############
print(5//3)             #1   int//int=int
print(5//2.4)           #2.0 float//float=float

print(5//(3+2j))        # TypeError: can't take floor of complex number
print(5.2//(3+2j))      # TypeError: can't take floor of complex number
print((2+1j)//(3+2j))  # TypeError: can't take floor of complex number

print(2//"World")       # TypeError: unsupported operand type(s) for //: 'int' and 'str'
print("Hello"//3.0)     # TypeError: unsupported operand type(s) for //: 'str' and 'float'
print("Hello"//(3+2j))  # TypeError: unsupported operand type(s) for //: 'str' and 'complex'
print("Hello"//"World") # TypeError: unsupported operand type(s) for //: 'str' and 'str'

# ################### ( % ) modulus ##############

print(5%3)            #2                     int%int=int
print(5%2.4)          #0.19999999999999973   int%float=float

print(5%(2+1j))       # TypeError: can't mod complex numbers
print(5.2%(3+2j))     # TypeError: can't mod complex numbers
print((2+1j)%(3+2j))  # TypeError: can't mod complex numbers

print(2%"World")       # TypeError: unsupported operand type(s) for %: 'int' and 'str'
print("Hello"%3.0)     # TypeError: unsupported operand type(s) for %: 'str' and 'float'
print("Hello"%(3+2j))  # TypeError: unsupported operand type(s) for %: 'str' and 'complex'
print("Hello"%"World") # TypeError: not all arguments converted during string formatting

# ################### ( ** ) exponentiation ##############
print(5**3)             #125              int**int=int
print(5**2.4)           #55.90169943749474   int**float=float
print(5.2**2.4)         #55.90169943749474   float**float=float

print(5**(3+2j))        # (-0.00033546262790251185-0.00033546262790251185j)   int**complex=complex
print(5.2**(3+2j))      # (-0.00033546262790251185-0.00033546262790251185j)   float**complex=complex
print((2+1j)**(3+2j))  # (-0.00033546262790251185-0.00033546262790251185j)   complex**complex=complex

print("Hello"**2)       # TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
print("Hello"**3.0)     # TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'float'
print("Hello"**(3+2j))  # TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'complex'
print("Hello"**"World") # TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'str'

# important points to remember:
# - Arithmetic operators in Python can be used with different data types, but the result depends on the types of the operands.
# - When performing operations between incompatible types, a TypeError will be raised.
# - Explicit type conversion is required to perform operations between different data types.

# simple track to remember the rules of arithmetic operators in Python: 
# 1. Operations between two integers result in an integer.
# 2. Operations between an integer and a float result in a float.
# 3. Operations between an integer or float and a complex number result in a complex number.
# 4. Operations between two complex numbers result in a complex number.
# 5. Operations between strings and numbers are not allowed unless explicit conversion is performed.