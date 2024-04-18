"""
Write a program to implement multithreading by extending Thread class in your program.
"""
from threading import Thread
class test(Thread):
    def __init__(self,msg):
        self.msg = msg
        Thread.__init__(self)
    def print_hello(self):
        for i in range(10):
            print(self.msg)
    def run(self):
        self.print_hello()
instance1 = test("instance 1")
instance2 = test("instance 2")
instance1.start()
instance2.start()
print('Main program')
