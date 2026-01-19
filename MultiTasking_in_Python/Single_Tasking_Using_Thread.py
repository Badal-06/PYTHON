# Import Thread class and sleep function
from threading import Thread
from time import sleep

# Define a class representing an exam
class MyExam:
    # Method that solves all three questions sequentially
    def solve_Question(self):
        self.q1()
        self.q2()
        self.q3()

    # Each question takes 3 seconds to solve (simulated with sleep)
    def q1(self):
        print("Question 1 solved")
        sleep(3)

    def q2(self):
        print("Question 2 solved")
        sleep(3)

    def q3(self):
        print("Question 3 solved")
        sleep(3)

# Create an object of MyExam
mye = MyExam()

# Create a thread that runs the solve_Question method
t = Thread(target=mye.solve_Question)

# Start the thread (it will call q1 → q2 → q3 with delays)
t.start()