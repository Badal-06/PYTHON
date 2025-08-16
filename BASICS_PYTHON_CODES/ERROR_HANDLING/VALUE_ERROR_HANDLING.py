# Define a function to safely get an integer from user input
def get_integer():
    try:
        # Take input from user
        user_input = input("Enter an integer: ")

        # Try to convert input into an integer
        number = int(user_input)

        # If conversion is successful, print the integer
        print("You entered:", number)

    except ValueError:
        # If conversion fails (e.g., user enters text), handle the error
        print("Error: That is not a valid integer.")

# Call the function
get_integer()