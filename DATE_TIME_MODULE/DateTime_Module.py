from datetime import datetime   # Importing datetime class from datetime module

# Creating datetime objects in different ways
dt1 = datetime(year=2025, month=8, day=5)                  # Date only (2025-08-05 00:00:00)
dt2 = datetime(year=2025, month=8, day=5, hour=18, minute=44)  # Date + specific time (2025-08-05 18:44:00)
dt3 = datetime(2025, 8, 5)                                 # Same as dt1, using positional arguments
dt4 = datetime(2025, 8, 5, 18, 44)                         # Same as dt2, using positional arguments

# Printing the datetime objects
print(dt1)   # Output: 2025-08-05 00:00:00
print(dt2)   # Output: 2025-08-05 18:44:00
print(dt3)   # Output: 2025-08-05 00:00:00
print(dt4)   # Output: 2025-08-05 18:44:00

# Accessing specific attribute of datetime
print(dt1.year)    # Prints only the year part → 2025

# Getting the current date and time
print(datetime.now())   # Prints the exact current system date and time