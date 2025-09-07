# Take input from user and convert it into an integer
Day_No = int(input("Enter a day number: "))

# Define a function to print the day name based on day number
def No_of_Day(Day_No):
    # Use match-case (Python 3.10+) for pattern matching
    match Day_No:
        case 1:
            print("Monday")
        case 2:
            print("Tuesday")
        case 3:
            print("Wednesday")
        case 4:
            print("Thursday")
        case 5:
            print("Friday")
        case 6:
            print("Saturday")
        case 7:
            print("Sunday")
        case _:   # Default case if input doesn’t match 1–7
            print("INVALID DAY NUMBER")

# Call the function with the user’s input
No_of_Day(Day_No)