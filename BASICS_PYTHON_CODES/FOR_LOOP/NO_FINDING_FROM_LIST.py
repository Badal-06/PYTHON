# List of numbers
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Number to search for in the list
x = 49

# Variable to keep track of the current index in the list
idx = 0

# Loop through each number in the list
for no in nums:
    # If the current number matches the search value 'x'
    if no == x:
        # Print a message showing the index where the number was found
        print("no. found at idx", idx)
    
    # Move to the next index
    idx += 1
