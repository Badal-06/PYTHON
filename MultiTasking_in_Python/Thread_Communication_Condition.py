# Import Thread class and Condition from threading module, sleep for delay
from threading import Thread, Condition
from time import sleep

# Shared list between producer and consumer
list = []

# Producer function
def produce():
    # Acquire the condition lock before modifying shared resource
    cv.acquire()
    for i in range(1, 6):
        list.append(i)   # Add an item to the list
        sleep(1)         # Simulate time taken to produce an item
        print('Item Produced...')
    cv.notify()          # Notify one waiting thread (consumer) that production is done
    cv.release()         # Release the lock

# Consumer function
def consume():
    # Acquire the condition lock before accessing shared resource
    cv.acquire()
    cv.wait(timeout=0)    # Wait until notified by producer (timeout=0 → returns immediately if not notified)
    cv.release()          # Release the lock
    print(list)           # Print the shared list

# Create a Condition object to synchronize producer and consumer
cv = Condition()

# Create threads for producer and consumer
t1 = Thread(target=produce)
t2 = Thread(target=consume)

# Start both threads
t1.start()
t2.start()