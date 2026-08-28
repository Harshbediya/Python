# ########### Logical Operators in Python ###########

# and, or, not
# They are used to combine conditional statements.
# The and operator returns True if both statements are true.
# The or operator returns True if at least one of the statements is true.
# The not operator returns True if the statement is false.

print(10>5 and 5<10) # True
print(10>5 or 5>10)  # True
print(not(10>5))     # False

# Important points to remember:
# - Logical operators are used to combine conditional statements.
# - The and operator returns True if both statements are true.
# - The or operator returns True if at least one of the statements is true.
# - The not operator returns True if the statement is false.

print(10**5**2) # 10000000000
# How to calculate 10**5**2 = 10**(5**2) = 10**25 = 10000000000
# How to solve rule of precedence in Python: Exponentiation is right-associative, so it is evaluated from right to left.
# so 5**2 is evaluated first, which is 25, and then 10**25 is evaluated, which is 10000000000.
# steps to think about it:
# 1. 5**2 = 25
# 2. 10**25 = 10000000000

######################################################################################################################################################

# ******** precedence of operators in Python: ********

# 1. ** (Exponentiation)
# 2. * / // % (Multiplication, Division, Floor Division, Modulus)
# 3. + - (Addition, Subtraction)
# 4. == != > < >= <= (Comparison Operators)
# 5. not (Logical NOT)
# 6. and (Logical AND)
# 7. or (Logical OR)
# order of precedence determines the order in which operators are evaluated in an expression.
# If an expression contains multiple operators, the operator with the highest precedence is evaluated first.
# if two operators have the same precedence, they are evaluated from left to right.
# if you want to change the order of precedence, you can use parentheses to group operators and operands together.

# Important points to remember:
# - The order of precedence determines the order in which operators are evaluated in an expression.
# - If an expression contains multiple operators, the operator with the highest precedence is evaluated first.
# - If two operators have the same precedence, they are evaluated from left to right.
# - Parentheses can be used to change the order of precedence.