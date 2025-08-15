# Take an integer input from the user (size of the square pattern)
n = int(input("Enter a number: "))

# Loop from 1 to n (inclusive) to print each row of the square
for i in range(1, n + 1):

    # If it's the first row or the last row
    if (i == 1 or i == n):
        # Print a full row of stars without line break at the end
        print("*" * n, end="")

    else:
        # Print the first star of the row (left border)
        print("*", end="")

        # Print spaces in the middle (n-2 spaces for hollow effect)
        print(" " * (n - 2), end="")

        # Print the last star of the row (right border)
        print("*", end="")

    # Move to the next line after printing each row
    print("")
