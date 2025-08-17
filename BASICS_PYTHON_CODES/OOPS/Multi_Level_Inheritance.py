# Define a parent class 'Father'
class Father:
    # Method of Father class
    def showF(self):
        print("Father Class Method ")

# Define a child class 'Son' that inherits from 'Father'
class Son(Father):
    # Method of Son class
    def showS(self):
        print("Son Class Method ")

# Define a child class 'GrandSon' that inherits from 'Son'
# (and indirectly from 'Father' as well → multi-level inheritance)
class GrandSon(Son):
    # Method of GrandSon class
    def showG(self):
        print("GrandSon Class Method ")

# Create an object of GrandSon class
g = GrandSon()

# Call methods from Father, Son, and GrandSon
g.showF()   # Inherited from Father
g.showS()   # Inherited from Son
g.showG()   # Defined in GrandSon