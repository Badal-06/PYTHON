# Function to find the length of the longest continuous uppercase substring
def longest_uppercase_substring(s):
    max_length = 0       # Stores the maximum length found so far
    current_length = 0   # Tracks the length of the current uppercase sequence

    # Loop through each character in the string
    for char in s:
        if char.isupper():  
            # If the character is uppercase, increase current sequence length
            current_length += 1
            # Update maximum length if current sequence is longer
            max_length = max(max_length, current_length)
        else:
            # If the character is not uppercase, reset the current length
            current_length = 0

    # Return the longest uppercase substring length found
    return max_length

# Take input from the user
s = input("Enter a string: ")

# Call the function and display the result
print("Length of the largest uppercase substring:", longest_uppercase_substring(s))
