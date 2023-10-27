from time import sleep

from threading import Thread

class hello(Thread):
    def run(self):
        for i in range(10):
            print('hello')
            sleep(0.1)

class hi(Thread):
    def run(self):
        for i in range(10):
            print('hi')
            sleep(0.1)

t1 = hello()
t2 = hi()

t1.start()
sleep(0.1)
t2.start()

t1.join()
t2.join()

print('bye')
