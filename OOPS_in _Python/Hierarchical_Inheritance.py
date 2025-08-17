# Define a parent class 'Father'
class Father:
    # Method inside Father class
    def showF(self):
        print("Father Class Method")

# Define a child class 'Son' that inherits from 'Father'
class Son(Father):
    # Method specific to Son class
    def showS(self):
        print("Son Class Method")

# Define another child class 'Daughter' that also inherits from 'Father'
class Daughter(Father):
    # Method specific to Daughter class
    def showD(self):
        print("Daughter Class Method")

# Create object of Son class
s = Son()
s.showS()   # Calls Son's own method
s.showF()   # Calls inherited method from Father

# Create object of Daughter class
d = Daughter()
d.showD()   # Calls Daughter's own method
d.showF()   # Calls inherited method from Father