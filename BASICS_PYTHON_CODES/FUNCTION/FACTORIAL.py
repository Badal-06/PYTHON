# Function to calculate factorial of a number using recursion
def fact(n):
    # Base case: factorial of 0 or 1 is always 1
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive case: n! = n × (n-1)!
        return n * fact(n - 1)

# Take an integer input from the user
n = int(input("Enter your number: "))

# Check if the number is negative
if n < 0:
    print("Factorial is not defined for negative numbers!")
else:
    # Calculate and print factorial for non-negative numbers
    print(f"factorial = {fact(n)}")
