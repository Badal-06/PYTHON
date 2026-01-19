# Import the Thread class from the threading module
from threading import Thread

# Define a class Mythread that inherits from the Thread class
class Mythread(Thread):
    # No custom behavior is added, so it behaves like a normal Thread
    pass

# Create an object of Mythread
t = Mythread()

# Print the name of the thread (default name like "Thread-1", "Thread-2", etc.)
print(t.name)