import time
from threading import Thread, Lock


class CheapRich:

    money = 100

    lock = Lock()

    def cheap(self):
        for _ in range(1000000):
            self.lock.acquire()
            self.money -= 10
            self.lock.release()
        print("Cheap done")

    def rich(self):
        for _ in range(1000000):
            self.lock.acquire()
            self.money += 10
            self.lock.release()
        print("Rich done")


ss = CheapRich()

t1 = Thread(target=ss.cheap)
t2 = Thread(target=ss.rich)

t1.start()
t2.start()

t1.join()
t2.join()

print("With Lock Final money: ", ss.money)


class CheapRich:

    money = 100

    def cheap(self):
        for _ in range(1000000):
            self.money -= 10
        print("Cheap done")

    def rich(self):
        for _ in range(1000000):
            self.money += 10
        print("Rich done")


ss = CheapRich()

t1 = Thread(target=ss.cheap)
t2 = Thread(target=ss.rich)

t1.start()
t2.start()

t1.join()
t2.join()

print("without Lock Final money: ", ss.money)
