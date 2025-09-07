# Define a class 'Student'
class Student:
    # Constructor to initialize student's name and roll number
    def __init__(self, n, r):
        self.name = n      # Instance variable for name
        self.roll = r      # Instance variable for roll number

    # Method to display student details
    def disp(self):
        print("Student Name:", self.name)
        print("Student Roll:", self.roll)

# Define another class 'User'
class User:
    # Static method (doesn't need self or cls)
    @staticmethod
    def show(s):   # 's' will be a Student object
        # Access attributes of Student object
        print("User Name:", s.name)
        print("User Roll:", s.roll)
        # Call the Student's disp() method
        s.disp()

# Create an object of Student
stu = Student('Badal', 101)

# Call static method of User class by passing Student object
User.show(stu)