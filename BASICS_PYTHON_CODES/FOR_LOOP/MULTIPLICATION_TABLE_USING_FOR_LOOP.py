# Take an integer input from the user (the number for the multiplication table)
n = int(input("Enter no: "))

# Loop from 1 to 10 to generate the multiplication table
for i in range(1, 11):
    # Print in the standard format: "n x i = result"
    print(f"{n} x {i} = {n * i}")
