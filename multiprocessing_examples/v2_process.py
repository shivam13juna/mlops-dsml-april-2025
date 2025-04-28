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


if __name__ == "__main__":
    multiprocessing.set_start_method("spawn")
    # spawn, fork, forkserver

    t = time.time()

    loop_count = 100

    processes = []

    for _ in range(loop_count):
        p = Process(target=intensive_work, args=())
        p.start()
        processes.append(p)  # collect all processes

    for p in processes:
        p.join()

    print("Parallel done in : ", "{:.8f}".format(time.time() - t))

    t = time.time()
    for _ in range(loop_count):
        intensive_work()

    print("Linear done in : ", "{:.8f}".format(time.time() - t))
