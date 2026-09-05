# A loop inside another loop is called a nested loop.
# Nested for loop

# Outer loop: runs from 1 to 3
for i in range(1, 4):

    # Inner loop: runs from 1 to 4
    for j in range(1, 5):

        # Print the value of i
        print(i, end=" ")
      
#------- break ---------
   
# Loop from 1 to 10
for i in range(1, 11):

    # Stop the loop when i becomes 4
    if i == 4:
        break

    # Print the value of i
    print(i, end=' ')
 
    
for i in range(1, 4):

    # Inner loop
    for j in range(1, 101):

        # Stop the inner loop when j becomes 3
        if j == 3:
            break

        # Print the value of i
        print(i, end=' ')
        
# -------- continue --------

for i in range(1, 11):

    # Skip the current iteration when i is 4
    if i == 4:
        continue

    # Print the value of i
    print(i, end=' ')
    
    
# -------- pass --------

n = int(input("n: "))

# Do nothing when n is 1
if n == 1:
    pass

else:
    print("Hello")