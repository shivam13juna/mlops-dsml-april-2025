import threading
import time
from threading import Thread


# def do_work():
# 	print("Starting work, oh screw it, sleeping for 1 second.")
# 	time.sleep(1)
# 	print("Done sleeping")


def do_work():
    # print("Starting work, oh screw it, sleeping for 1 second.")
    # time.sleep(1)
    i = 0

    for _ in range(10000):
        i += 1
    # print("Done sleeping")


# execute it sequentially
loop_count = 100

ti = time.time()
for _ in range(loop_count):
    for i in range(5):
        do_work()
print("Sequential execution took: ", time.time() - ti)


# execute it in parallel using threads

ti = time.time()

threads = []
for _ in range(loop_count):
    for i in range(5):
        t = Thread(target=do_work)
        threads.append(t)
        t.start()
for t in threads:
    t.join()

print("Parallel execution took: ", time.time() - ti)
