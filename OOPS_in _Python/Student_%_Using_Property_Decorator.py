# Define a class 'student'
class student:
    # Constructor to initialize marks in physics, chemistry, and math
    def __init__(self, phy, chem, math):
        self.phy = phy      # Physics marks
        self.chem = chem    # Chemistry marks
        self.math = math    # Math marks

    # Property decorator converts a method into a read-only attribute
    @property
    def per(self):
        # Calculate percentage and return as string with '%'
        return str((self.phy + self.chem + self.math) / 3) + "%"

# Create object of student with marks
s1 = student(98, 97, 99)

# Access 'per' like an attribute, though it's actually a method
print(s1.per)   # Prints average = (98+97+99)/3 %

# Update physics marks
s1.phy = 95

# Percentage automatically updates (because it's calculated dynamically)
print(s1.per)