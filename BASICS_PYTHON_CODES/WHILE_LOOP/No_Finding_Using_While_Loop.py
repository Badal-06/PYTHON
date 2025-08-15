# Create a tuple of numbers
nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

# The number we want to search for
x = 49

# Initialize index counter
i = 0

# Loop until the end of the tuple
while i < len(nums):
    # Check if the current element matches x
    if nums[i] == x:
        print("found at idx", i)  # Print the index where number is found
        break                     # Exit the loop once found
    else:
        print("finding")           # Print message if not found yet
    
    # Move to the next index
    i += 1
