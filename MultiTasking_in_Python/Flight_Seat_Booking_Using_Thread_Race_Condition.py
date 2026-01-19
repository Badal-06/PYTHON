# Import Thread class and current_thread function
from threading import Thread, current_thread

# Define a Flight class to handle seat reservation
class Flight:
    def __init__(self, available_seat):
        # Store the number of available seats
        self.available_seat = available_seat

    # Method to reserve seats
    def reserve(self, need_seat):
        # Show current available seats
        print("Available seat:", self.available_seat)

        # Check if required seats are available
        if self.available_seat >= need_seat:
            # Get the name of the current running thread (person)
            name = current_thread().name
            print(f"{need_seat} seat is allotted for {name}")

            # Reduce available seats
            self.available_seat -= need_seat
        else:
            print("Sorry! All seats have been allotted")

# Create a Flight object with 1 seat
f = Flight(1)

# Create two threads trying to reserve the seat
t1 = Thread(target=f.reserve, args=(1,), name="Badal")
t2 = Thread(target=f.reserve, args=(1,), name="Harsh")

# Start both threads
t1.start()
t2.start()