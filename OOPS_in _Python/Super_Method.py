# Define parent class 'Father'
class Father:
    # Constructor of Father class
    def __init__(self):
        print("Father Class Constructor")

    # Instance method of Father class
    def show(self):
        print("Father Class Instance Method")

# Define child class 'Son' that inherits from Father
class Son(Father):
    # Constructor of Son class
    def __init__(self):
        # Call the constructor of the parent class (Father) using super()
        super().__init__()
        print("Son Class Constructor")

    # Instance method of Son class
    def disp(self):
        print("Son Class Instance Method")

# Create object of Son class
s = Son()   # This will first call Father's constructor (via super()), then Son's constructor