# Import Thread class and current_thread() function from threading module
from threading import Thread, current_thread

# Define a function that will run inside a child thread
def disp():
    # Print the current thread's default name
    print("Child Thread Name :", current_thread().name)
    
    # Change the current thread's name
    current_thread().name = 'doc Thread'
    
    # Print the new name after modification
    print("New Child Thread Name :", current_thread().name)

# Create a thread without giving it a name explicitly
# It will get a default name like "Thread-1"
t = Thread(target=disp)
t.start()   # Start this child thread (runs disp)

# Create another thread but explicitly give it a name "New Thread"
t = Thread(target=disp, name='New Thread')

# Print the name of this thread BEFORE starting it
print("Latest thread Name:", t.name)

# Print the name of the main thread (usually "MainThread")
print("Main Thread Name:", current_thread().name)