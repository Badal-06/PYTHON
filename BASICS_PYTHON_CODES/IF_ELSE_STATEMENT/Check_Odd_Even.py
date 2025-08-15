# Take an integer input from the user
num = int(input("Enter your number: "))

# Find the remainder when the number is divided by 2
rem = num % 2

# If the remainder is 0, then the number is even
if rem == 0:
    print("even")
# Otherwise, the number is odd
else:
    print("odd")
