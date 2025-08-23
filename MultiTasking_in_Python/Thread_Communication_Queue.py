# Import Thread class, Queue, and sleep for delays
from threading import Thread
from queue import Queue
from time import sleep

# Producer class
class Producer:
    def __init__(self):
        # Create a queue to store produced items
        self.q = Queue()

    # Produce 5 items
    def produce(self):
        for i in range(1, 6):
            print('Item Produced', i)
            self.q.put(i)    # Add item to queue
            sleep(1)         # Simulate production time

# Consumer class
class Consumer:
    def __init__(self, prod):
        self.prod = prod   # Reference to producer object

    # Consume 5 items
    def consume(self):
        for i in range(1, 6):
            # Get item from producer's queue (blocks if empty)
            print('Item received', self.prod.q.get())

# Create producer and consumer objects
p = Producer()
c = Consumer(p)

# Create threads for producer and consumer
t1 = Thread(target=p.produce)
t2 = Thread(target=c.consume)

# Start both threads
t1.start()
t2.start()