# Initialize counter variable
i = 1

# Loop until i reaches 10
while i <= 10:
    # Check if the number is odd
    if (i % 2 != 0):
        # Increment i and skip the rest of the loop for odd numbers
        i += 1
        continue
    
    # Print the even number
    print(i)
    
    # Increment i to move to the next number
    i += 1
