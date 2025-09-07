# Define a class named 'Mobile'
class Mobile:
    # Constructor (__init__) method to initialize object attributes
    def __init__(self):
        # Instance variable 'model' initialized with default value
        self.model = 'RealMe X'

    # Instance method to display the model name
    def show_model(self):
        print(self.model)

# Create three objects of Mobile class
realme = Mobile()
redmi = Mobile()
oppo = Mobile()

# Print model name of each object (all will print "RealMe X")
print(realme.model)
print(redmi.model)
print(oppo.model)
print()

# Change the model of the 'redmi' object only
redmi.model = 'Redmi 10s'

# Print again to show that only redmi's model has changed
print(realme.model)   # Still "RealMe X"
print(redmi.model)    # Now "Redmi 10s"
print(oppo.model)     # Still "RealMe X"