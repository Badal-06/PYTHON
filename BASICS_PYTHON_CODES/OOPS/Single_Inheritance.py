# Define parent class 'Father'
class Father:
    # Class variable (shared by all objects of Father and its subclasses)
    money = 1000

    # Instance method (needs self → works with object)
    def show(self):
        print("Parents Class Instance Method")

    # Class method (needs cls → works with class itself)
    @classmethod
    def showmoney(cls):
        print("Parent Class Class Method:", cls.money)

# Define child class 'Son' that inherits from 'Father'
class Son(Father):
    # Instance method of Son
    def disp(self):
        print("Child Class Instance Method")

# Create object of Son class
s = Son()

# Call Son's instance method
s.disp()

# Call inherited instance method from Father
s.show()

# Call inherited class method from Father
s.showmoney()