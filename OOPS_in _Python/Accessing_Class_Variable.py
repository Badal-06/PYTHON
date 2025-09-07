# Define a class named 'Mobile'
class Mobile:
    # Class variable (shared by all objects of the class)
    fp = 'yes'

    # Class method (takes 'cls' as a parameter instead of 'self')
    # 'cls' refers to the class itself, not an instance
    @classmethod
    def is_fp(cls):
        # Access the class variable using 'cls'
        print(cls.fp)

# Create an object of the class 'Mobile'
realme = Mobile()

# Call the class method directly using the class name
# (You can also call it with 'realme.is_fp()')
Mobile.is_fp()