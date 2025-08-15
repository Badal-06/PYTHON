# Take an integer input from the user
n = int(input("Enter a number: "))

# Initialize the factorial result variable to 1
fact = 1

# Loop from 1 to n (inclusive) to calculate factorial
for i in range(1, n + 1):
    # Multiply 'fact' by the current number 'i'
    fact *= i

# Print the final factorial value
print("fact:", fact)
