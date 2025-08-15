# Take a string input from the user
str = input("Enter the string: ")

# Initialize counter variables for alphabets and digits
no_of_alphabets = 0
no_of_digits = 0

# Loop through each character in the string using its index
for i in range(len(str)):
    # Get the character at index 'i'
    char = str[i]

    # Check if the character is an alphabet (A-Z or a-z)
    if char.isalpha():
        no_of_alphabets += 1  # Increase alphabet count by 1

    # Check if the character is a digit (0-9)
    elif char.isdigit():
        no_of_digits += 1  # Increase digit count by 1

    # Increment 'i' 
    i += 1

# Print the total number of alphabets found in the string
print(f"No. of alphabets in the given string: {no_of_alphabets}")

# Print the total number of digits found in the string
print(f"No. of Digits in the given string: {no_of_digits}")
