import pickle, Pick_Class   # Import pickle module and custom module PickClass

# Ask user how many student records they want to enter
n = int(input("Enter Number of Student: "))

# Open file 'student.data' in binary write mode
with open("student.data", mode="wb") as f:
    for i in range(n):   # Loop for each student
        # Take input for student details
        name = input("Enter Student Name: ")
        roll = int(input("Enter Roll: "))
        address = input("Enter Address: ")

        # Create a Student object (class is defined inside PickClass module)
        stu1 = PickClass.Student(name, roll, address)

        # Serialize (pickle) the object and write it into the file
        pickle.dump(stu1, f)

# After loop ends
print("Pickling Done!!")   # Confirmation message