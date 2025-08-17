# Import ABC (Abstract Base Class) and abstractmethod from abc module
from abc import ABC, abstractmethod

# Define an abstract base class named 'DefenceForce'
class DefenceForce(ABC):
    # Abstract method that must be implemented by all subclasses
    @abstractmethod
    def area(self):
        pass

    # A normal (concrete) method that can be inherited by all subclasses
    def gun(self):
        print("Gun = AK47")

# Subclass representing Army, inheriting from DefenceForce
class Army(DefenceForce):
    # Implementing the abstract method 'area'
    def area(self):
        print("Army Area = Land")

# Subclass representing AirForce, inheriting from DefenceForce
class AirForce(DefenceForce):
    # Implementing the abstract method 'area'
    def area(self):
        print("AirForce Area = Sky")

# Subclass representing Navy, inheriting from DefenceForce
class Navy(DefenceForce):
    # Implementing the abstract method 'area'
    def area(self):
        print("Navy Area = Sea")

# Create objects of Army, AirForce, and Navy
a = Army()
af = AirForce()
n = Navy()

# Call gun() and area() methods using Army object
a.gun()
a.area()

# Call gun() and area() methods using AirForce object
af.gun()
af.area()

# Call gun() and area() methods using Navy object
n.gun()
n.area()