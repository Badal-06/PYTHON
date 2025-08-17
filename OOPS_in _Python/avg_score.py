# Define a class named 'student'
class student:
    # Constructor to initialize name and marks list
    def __init__(self, name, marks):
        self.name = name          # Instance variable to store student's name
        self.marks = marks        # Instance variable to store list of marks

    # Method to calculate and print average marks
    def get_avg(self):
        sum = 0                   # Variable to store total marks
        # Loop through each mark in the marks list and add to sum
        for val in self.marks:
            sum += val
        # Print the average (sum divided by 3 since student has 3 subjects)
        print("Hi", self.name, "your average score is", sum / 3)

# Create an object 's1' of student class with name and marks
s1 = student("badal", [98, 99, 97])

# Call the method to calculate and print average marks
s1.get_avg()