# Take user input and store it in variable 'original' (also in 'a' for processing)
original = a = int(input("Enter the Number: "))

# Initialize variable to store reversed number
Reverse = 0

# Loop until 'a' becomes 0
while a > 0:
    r = a % 10                # Get the last digit of 'a'
    Reverse = Reverse * 10 + r  # Append last digit to Reverse
    a //= 10                  # Remove the last digit from 'a'

# Check if original number and reversed number are the same
if original == Reverse:
    print(f"{original} IS PALINDROME!!")  # It's the same forwards and backwards
else:
    print(f"{original} IS NOT PALINDROME??")  # Not the same forwards and backwards