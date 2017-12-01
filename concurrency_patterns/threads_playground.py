from threading import Thread
import time


def counter(n):
    for i in range(n):
        print(i)
        time.sleep(3)


def reverse_counter(n):
    for i in range(n, 0, -1):
        print(i)
        time.sleep(5)

t1 = Thread(target=counter, args=(10,))
t2 = Thread(target=reverse_counter, args=(10,))
t1.start()
t2.start()
t1.join()
#t2.join()


