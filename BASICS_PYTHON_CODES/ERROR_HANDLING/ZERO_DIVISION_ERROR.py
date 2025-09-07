# Define a function to divide two numbers safely
def divide_numbers(a, b):
    try:
        # Try dividing 'a' by 'b'
        result = a / b
        print("Result:", result)
    except ZeroDivisionError:  
        # Handle the case when denominator 'b' is zero
        print("Error: Cannot divide by zero.")

# Function call with valid division (10 ÷ 2 = 5.0)
divide_numbers(10, 2)

# Function call with division by zero (will trigger the exception)
divide_numbers(5, 0)