from datetime import timedelta, date   # Import timedelta and date classes

d = int(input("Date After : "))        # Ask user how many days to add
f = timedelta(d)                       # Create a timedelta object with given number of days
c = date.today()                       # Get today's date
print(f"Date After {d} Days : ", f + c)  # Add timedelta to today's date and print result