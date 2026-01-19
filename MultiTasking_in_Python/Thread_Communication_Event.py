# Import Thread class and Event from threading module, sleep for delays
from threading import Thread, Event
from time import sleep

# Function to simulate traffic light switching
def light_switch():
    sleep(3)         # Wait 3 seconds before turning green
    e.set()          # Set the event → signals that green light is ON
    print('Green Light ON')
    sleep(5)         # Keep green light for 5 seconds
    print('Red Light ON')
    e.clear()        # Clear the event → signals that red light is ON

# Function to simulate traffic behavior
def traffic():
    e.wait()         # Wait until event is set (green light ON)
    while e.is_set():  # While green light is ON
        print('You can GO....')
    print('Program Done')

# Create an Event object to coordinate threads
e = Event()

# Create threads for traffic light and traffic
t1 = Thread(target=light_switch)
t2 = Thread(target=traffic)

# Start both threads
t1.start()
t2.start()