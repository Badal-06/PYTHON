# Code to determine the grade of a student based on marks

# Take integer input for marks from the user
marks = int(input("marks: "))

# If marks are 90 or above, grade is A
if marks >= 90:
    print("A")

# If marks are between 80 and 89, grade is B
elif marks >= 80:
    print("B")

# If marks are between 70 and 79, grade is C
elif marks >= 70:
    print("C")

# If marks are below 70, grade is D
else:
    print("D")
