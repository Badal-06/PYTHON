# Define a class named 'Circle'
class Circle:
    # Constructor to initialize radius when creating a Circle object
    def __init__(self, radius):
        self.radius = radius   # Instance variable to store radius

    # Method to calculate the area of the circle
    def area(self):
        return (22/7) * self.radius ** 2   # Formula: πr² (using 22/7 as π)

    # Method to calculate the perimeter (circumference) of the circle
    def per(self):
        return 2 * (22/7) * self.radius    # Formula: 2πr (using 22/7 as π)

# Create an object 'c1' of Circle class with radius 49
c1 = Circle(49)

# Print the area of the circle
print(c1.area())

# Print the perimeter (circumference) of the circle
print(c1.per())