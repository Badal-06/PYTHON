from time import localtime   # Importing localtime function from time module

m = localtime()   # Getting the current local time (returns a struct_time object)

# Printing the date in the format: day/month/year
print("Date = ", end = " ")         # Print label "Date =" without moving to a new line
print(m.tm_mday, end ="/")          # Print current day of the month, followed by "/"
print(m.tm_mon, end ="/")           # Print current month, followed by "/"
print(m.tm_year)                    # Print current year

# Printing the time in the format: hour:minute:second
print("Time = ", end = " ")         # Print label "Time =" without moving to a new line
print(m.tm_hour, end =":")          # Print current hour, followed by ":"
print(m.tm_min, end =":")           # Print current minute, followed by ":"
print(m.tm_sec)                     # Print current second