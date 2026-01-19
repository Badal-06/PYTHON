# Import Thread class from threading module
from threading import Thread

# Define a function to be executed by the thread
def disp():
    print("Daemon Thread")

# Create a Thread object with target function disp
t1 = Thread(target=disp)

# By default, a thread is NOT a daemon thread (so daemon = False)
print('Before:', t1.daemon)

# Change the thread type to Daemon (background thread)
t1.daemon = True

# Now daemon property is True
print('After:', t1.daemon)

# Start the thread (this will run disp)
t1.start()