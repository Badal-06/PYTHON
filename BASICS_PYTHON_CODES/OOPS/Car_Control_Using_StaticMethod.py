# Define a parent class 'car'
class car:
    # Static method to start the car
    @staticmethod
    def start():
        print("car started")

    # Static method to stop the car
    @staticmethod
    def stop():
        print("car stopped")

# Define a child class 'toyotaCar' that inherits from 'car'
class toyotaCar(car):
    # Constructor to initialize car name
    def __init__(self, name):
        self.name = name

# Create two objects of 'toyotaCar'
car1 = toyotaCar("Fortuner")
car2 = toyotaCar("Prius")

# Call the static method 'start' using object 'car1'
# Even though 'start' does not depend on any instance, it can still be called using an object
print(car1.start())   # Prints "car started" and then 'None' because 'print()' is used