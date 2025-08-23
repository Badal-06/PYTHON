# Import the Thread class from the threading module
from threading import Thread

# Define a simple class (not inheriting from Thread)
class Mythread:
    # A method that takes two arguments and prints them
    def disp(self, a, b):
        print(a, b)

# Create an object of Mythread
myt = Mythread()

# Create a Thread object
# target = function to run inside the thread
# args = tuple of arguments to pass into the function
t = Thread(target=myt.disp, args=(10, 20))

# Start the thread (this will internally call myt.disp(10, 20))
t.start()