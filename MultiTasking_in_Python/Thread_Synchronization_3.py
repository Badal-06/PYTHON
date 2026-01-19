# Import everything from threading module
from threading import *

# Define a Flight class
class Flight:
    def __init__(self, available_seat):
        # Number of seats available
        self.available_seat = available_seat

        # Create a semaphore with a maximum of 2 concurrent accesses
        self.l = Semaphore(2)
        print(self.l)  # Print semaphore object (for debugging)

    # Method to reserve seats
    def reserve(self, need_seat):
        # Acquire the semaphore (decrement counter)
        self.l.acquire()

        # Print current semaphore value (how many permits are left)
        print(self.l._value)

        # Show current available seats
        print("Available seat:", self.available_seat)

        # Check if seats are enough
        if self.available_seat >= need_seat:
            name = current_thread().name
            print(f"{need_seat} seat is allotted for {name}")
            self.available_seat -= need_seat
        else:
            print("Sorry! All seats have been allotted")

        # Release the semaphore (increment counter)
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