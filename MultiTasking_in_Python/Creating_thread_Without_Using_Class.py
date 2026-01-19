# Import the Thread class from the threading module
from threading import Thread

# Define a function that will be executed by the child thread
def disp():
    for i in range(5):
        print("Child Thread")

# Create a Thread object
# target = function to run inside the thread (here, disp function)
t = Thread(target=disp)

# Start the child thread (this will call disp())
t.start()

# Meanwhile, the main thread continues executing this loop
for i in range(5):
    print("Main Thread")