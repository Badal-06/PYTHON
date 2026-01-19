from datetime import date   # Importing date class from datetime module

# Taking user input for birth date, month, and year
d = int(input("Enter Your Birth Date : "))
m = int(input("Enter Your Birth Month : "))
y = int(input("Enter Your Birth Year : "))

# Creating a date object for date of birth
dob = date(y, m, d)

# Getting today's date
t = date.today()

# Calculating age:
# Subtract birth year from current year
# Then adjust by subtracting 1 if today's month/day is before birthday in the current year
age = t.year - dob.year - ((t.month, t.day) < (dob.month, dob.day))

# Printing the age in years
print("Your Age is -->", age, "Years")