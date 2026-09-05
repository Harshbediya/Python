# Type Casting in Python
# Type casting is the process of converting a variable from one data type to another. In Python, you can use built-in functions 
# like int(), float(), str(), etc., to perform type casting.

a="34"
b=int(a)
print(b)   
print(type(b))

d=float(a)
print(d)

c=complex(a)
print(c)

# boolean_value, bool(a)
# print(boolean_value)
boolean_value = bool(a)
print(boolean_value)

ab=(1+2j)
bb=bool(ab)
print(bb)