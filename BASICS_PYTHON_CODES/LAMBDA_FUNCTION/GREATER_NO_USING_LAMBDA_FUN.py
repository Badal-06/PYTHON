# Take input from the user and convert it into an integer
no1 = int(input("Enter 1st number: "))
no2 = int(input("Enter 2nd number: "))

# Define a lambda function to find the greater number between x and y
greater = lambda x, y: x if x > y else y

# Print the greater number using the lambda function
print("Greater number is:", greater(no1, no2))