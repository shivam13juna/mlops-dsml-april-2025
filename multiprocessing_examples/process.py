import multiprocessing
import time
from multiprocessing import Process


def do_work():
	# print("Starting work")
	# print(threading.activeCount())
	time.sleep(1)


def intensive_work():
	i = 0
	for _ in range(2000000):
		i += 1
	# print("Finished work")


# let's execute it sequentially

ti = time.time()
for _ in range(10):
	do_work()

print("Sequential execution took: ", time.time() - ti)

multiprocessing.set_start_method("spawn")
# let's execute it in parallel using processes

ti = time.time()
processes = []
for _ in range(10):
	p = Process(target=do_work)
	processes.append(p)
	p.start()


for p in processes:
	p.join()
print("Parallel execution took: ", time.time() - ti)