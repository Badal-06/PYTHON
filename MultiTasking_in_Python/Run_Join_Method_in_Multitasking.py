# Import Thread class from threading module
from threading import Thread

# Create a class Mythread that inherits from Thread
class Mythread(Thread):
    # Override the run() method (this is what executes when thread starts)
    def run(self):
        for i in range(5):
            print("Child Thread")

# Create an object of Mythread
t = Mythread()

# Start the child thread → internally calls run()
t.start()

# Wait until child thread finishes execution before continuing
t.join()

# After child thread is done, the main thread executes this loop
for i in range(5):
    print("Main Thread")