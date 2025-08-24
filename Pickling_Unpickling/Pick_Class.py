# Defining a Student class
class Student:
    # Constructor (initializer) method
    def __init__(self, name, roll, address):
        # Instance variables to store student details
        self.name = name
        self.roll = roll
        self.address = address

    # Method to display student details
    def disp(self):
        print(f"Name: {self.name}")       # Print student name
        print(f"Roll: {self.roll}")       # Print student roll number
        print(f"Address: {self.address}") # Print student address