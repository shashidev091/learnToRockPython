from threading import Thread
from time import sleep


def divide(a, b):
    return a / b


try:
    c = divide(10, 0)
except Exception as ex:
    print(ex, 'is wrong')


class MultiThreading(Thread):
    def __init__(self):
        super().__init__()
        print('Multithreading')

    def run(self):
        for i in range(5):
            print('hi')
            sleep(1)


class MultiThreading2(Thread):
    def run(self):
        for i in range(5):
            print('hello')
            sleep(1)


mulM1 = MultiThreading()
mulM2 = MultiThreading2()
mulM1.start()
mulM2.start()


a_list = [1, 3, 4, 4, 9, 1, 4, 3]
new_list = []

for item in a_list:
    if item not in new_list:
        new_list.append(item)

print(new_list)
