# Function to capitalize the first letter of each word in a string
def capitalize(newstr):
    # .title() converts the first letter of each word to uppercase 
    # and the rest of the letters to lowercase
    return newstr.title()

# Take input from the user
str = input("Enter the string: ")

# Call the capitalize() function and print the result
print(capitalize(str))
