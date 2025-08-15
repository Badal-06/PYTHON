# Function to find the largest number among three given numbers
def largest_number(a, b, c):
    # Check if 'a' is greater than both 'b' and 'c'
    if (a > b) and (a > c):
        print("a is Largest")
    # Check if 'b' is greater than both 'a' and 'c'
    elif (b > a) and (b > c):
        print("b is Largest")
    # If neither of the above is true, then 'c' is the largest
    else:
        print("c is largest")

# Taking user input for all three numbers
a = int(input("a="))
b = int(input("b="))
c = int(input("c="))

# Calling the function and printing the result (function itself prints output)
print(largest_number(a, b, c))
