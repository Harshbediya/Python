# These are relational operators in Python. They are used to compare two values and return a boolean result (True or False).
# == : Equal to
# != : Not equal to
# < : Less than
# > : Greater than
# <= : Less than or equal to
# >= : Greater than or equal to

a,b,c=10,20,30
print(a==b,a==c) # False False
print(a!=b,a!=c) # True True
print(a<b,a<c)   # True True
print(b>c,b>a)   # False False
print(a<=c)      #True
print(a>=c)      #False

print(100=="don") # False 
print(1=="1")     # False
print(100!='don') # True
print(100<3.5)    # False

a,b,c=30,40,30
print(a>b or not b**3==500 and not b<c) # True 

# How to solve the above expression:
# 1. Evaluate b**3==500: 40**3 = 64000, so this is False
# 2. Evaluate not b**3==500: not False = True
# 3. Evaluate b<c: 40<30 = False
# 4. Evaluate not b<c: not False = True
# 5. Evaluate a>b: 30>40 = False
# 6. Evaluate a>b or not b**3==500: False or True = True
# 7. Evaluate (a>b or not b**3==500) and not b<c: True and True = True

####################################################################################################################################################

# ******* Note ******: The relational operators can be used with different data types, but
# the result depends on the types of the operands. For example, comparing a string with an integer will always return False.
# if you compare two different data types, Python will raise a TypeError.
# Important points to remember: 
  # - Relational operators are used to compare values and return a boolean result.
  # - The result of a comparison depends on the types of the operands.
  # - Comparing different data types may lead to unexpected results or errors.
  
# most importantly, relational operators are fundamental in programming for making decisions and controlling the flow of 
# a program based on conditions.

# Most Important point to remember:
# - Relational operators are used to compare values and return a boolean result (True or False)
# - They are essential for decision-making and controlling the flow of a program based on conditions.