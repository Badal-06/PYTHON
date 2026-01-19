# Import everything from threading module
from threading import *

# Define a Flight class
class Flight:
    def __init__(self, available_seat):
        # Number of seats available
        self.available_seat = available_seat

        # Create a reentrant lock (RLock)
        # Allows the same thread to acquire the lock multiple times safely
        self.l = RLock()
        print(self.l)  # Print lock object for debugging

    # Method to reserve seats
    def reserve(self, need_seat):
        # Acquire the RLock before accessing/modifying shared resource
        self.l.acquire()
        print(self.l)  # Print lock object after acquiring

        # Print current available seats
        print("Available seat:", self.available_seat)

        # Check if required seats are available
        if self.available_seat >= need_seat:
            # Get the name of the current thread
            name = current_thread().name
            print(f"{need_seat} seat is allotted for {name}")

            # Reduce available seats
            self.available_seat -= need_seat
        else:
            print("Sorry! All seats have been allotted")

        # Release the lock so other threads can access
        self.l.release()

# Create a Flight object with 2 seats
f = Flight(2)

# Create 3 threads trying to reserve seats
t1 = Thread(target=f.reserve, args=(1,), name="Badal")
t2 = Thread(target=f.reserve, args=(1,), name="Harsh")
t3 = Thread(target=f.reserve, args=(1,), name="Nevid")

# Start all threads
t1.start()
t2.start()
t3.start()