# Import Thread class from threading module
from threading import Thread

# Create a class Mythread that inherits from Thread
class Mythread(Thread):
    # Constructor (called when object is created)
    def __init__(self):
        # Call parent (Thread) class constructor to properly initialize
        Thread.__init__(self)
        print("Child Thread Constructor")

    # Override run() method (executed when thread starts)
    def run(self):
        pass   # No task defined here

# Create an object of Mythread
t = Mythread()

# Start the child thread (this internally calls run(), but run is empty)
t.start()

# Main thread continues execution
print("Main Thread")