# Function to find the largest number among three
def largest_number(a, b, c):
    # Check if 'a' is greater than both 'b' and 'c'
    if (a > b) and (a > c):
        return "a is Largest"
    
    # Check if 'b' is greater than both 'a' and 'c'
    elif (b > a) and (b > c):
        return "b is Largest"
    
    # If neither 'a' nor 'b' is largest, then 'c' must be largest
    else:
        return "c is Largest"

# Take input for three numbers from the user
a = int(input("a = "))  # Get integer value for 'a'
b = int(input("b = "))  # Get integer value for 'b'
c = int(input("c = "))  # Get integer value for 'c'

# Call the function and print the returned result
print(largest_number(a, b, c))