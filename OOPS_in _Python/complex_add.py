# Define a class named 'complex' to represent complex numbers
class complex:
    # Constructor to initialize real and imaginary parts
    def __init__(self, real, img):
        self.real = real    # Instance variable for real part
        self.img = img      # Instance variable for imaginary part

    # Method to display the complex number in proper format
    def showNumber(self):
        print(self.real, "i +", self.img, "j")

    # Operator overloading for '+' (addition of two complex numbers)
    def __add__(self, num2):
        # Add real parts
        newReal = self.real + num2.real
        # Add imaginary parts
        newImg = self.img + num2.img
        # Return a new complex object as the result
        return complex(newReal, newImg)

# Create first complex number: 1i + 2j
num1 = complex(1, 2)
num1.showNumber()

# Create second complex number: 4i + 6j
num2 = complex(4, 6)
num2.showNumber()

# Use overloaded '+' operator to add num1 and num2
num3 = num1 + num2

# Display the result (5i + 8j)
num3.showNumber()