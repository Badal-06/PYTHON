# Take an integer input from the user (height of the pyramid)
n = int(input("Enter a number: "))

# Loop through each row from 1 to n
for i in range(1, n + 1):

    # Print spaces before the stars (for pyramid alignment)
    # 'n - i' spaces ensure that the stars are centered
    print(" " * (n - i), end="")

    # Print stars: for row i, there are (2*i - 1) stars
    # This creates an odd number of stars for each row (1, 3, 5, 7, ...)
    print("*" * (2 * i - 1), end="")

    # Move to the next line after printing spaces and stars
    print("")
