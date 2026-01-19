# Import Thread class from threading module
from threading import Thread

# Define a Hotel class
class Hotel:
    def __init__(self, t):
        # Store the task message (either "Take Order" or "Serve Order")
        self.t = t

    # Method to print the task 5 times
    def food(self):
        for i in range(1, 6):
            print(self.t, i)

# Create two Hotel objects with different tasks
h1 = Hotel('Take Order From Table')
h2 = Hotel('Serve Order to Table')

# Create two threads and assign different tasks
t1 = Thread(target=h1.food)    # Thread for taking orders
t2 = Thread(target=h2.food)    # Thread for serving orders

# Start both threads
t1.start()
t2.start()