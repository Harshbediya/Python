# Example 1: Print numbers from 1 to 10
i = 1

# Run the loop while i is less than 11
while i < 11:
    # Print the value of i
    print(i, end=' ')
    
    # Increase i by 1
    i += 1


# Example 2: Print numbers from 10 to 1
n = 10

# Run the loop while n is greater than 0
while n > 0:
    # Print the value of n
    print(n, end=' ')
    
    # Decrease n by 1
    n -= 1


# Nested loop
i = 1

# Outer while loop
while i < 4:
    # Initialize j for the inner loop
    j = 1

    # Inner while loop
    while j < 5:
        # Print the value of i
        print(i, end=' ')
        
        # Increase j by 1
        j += 1

    # Increase i by 1
    i += 1