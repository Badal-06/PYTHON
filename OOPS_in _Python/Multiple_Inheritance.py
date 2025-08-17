# Define a parent class 'Father'
class Father:
    # Method inside Father class
    def showF(self):
        print("Father Class Method")

# Define another parent class 'Mother'
class Mother:
    # Method inside Mother class
    def showM(self):
        print("Mother Class Method")

# Define a child class 'Son' that inherits from both Father and Mother
# This is an example of multiple inheritance
class Son(Father, Mother):
    # Method specific to Son class
    def showS(self):
        print("Son Class Method")

# Create object of Son class
s = Son()

# Call methods from Father, Mother, and Son
s.showF()   # Inherited from Father
s.showM()   # Inherited from Mother
s.showS()   # Defined in Son