from datetime import timedelta, date   # Importing timedelta and date classes from datetime module

f = timedelta(days=10)   # Creating a timedelta object that represents 10 days
c = date.today()         # Getting the current date
print(f + c)             # Adding 10 days to today's date and printing the result