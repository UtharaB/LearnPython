import os
import time
import multiprocessing as mp

def child_task(i):
    print(f"Child {i} started with PID {os.getpid()}")
    time.sleep(2)  # simulate some work
    print(f"Child {i} finished with PID {os.getpid()}")

if __name__ == "__main__":
    print(f"Parent PID {os.getpid()} starting...")

    processes = []
    for i in range(3):   # spawn 3 children
        p = mp.Process(target=child_task, args=(i,))
        p.start()
        processes.append(p)
        print(f"Parent spawned Child {i}")

    print("Parent waiting for children...")
    for p in processes:
        p.join()

    print(f"Parent PID {os.getpid()} all children done.")