# Define outer class 'Army'
class Army:
    def __init__(self):
        # Instance variable of Army
        self.name = 'Badal'
        # Creating an object of inner class 'Gun' inside Army
        self.gn = self.Gun()
    
    # Method of Army class
    def show(self):
        print("Name:", self.name)

    # Define inner class 'Gun'
    class Gun:
        def __init__(self):
            # Instance variables of Gun
            self.name = 'AK47'
            self.capacity = '75 Rounds'
            self.length = '34.3 In'

        # Method of Gun class to display details
        def disp(self):
            print("Gun Name:", self.name)
            print("Capacity:", self.capacity)
            print("Length:", self.length)

# Create object of Army
a = Army()

# Access Army's instance variable
print(a.name)

# Call method from Army class
a.show()

# Access the inner class object created inside Army
g = a.gn

# Access Gun's instance variable
print(g.name)

# Call method from Gun class
g.disp()