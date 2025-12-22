# Code to understand threading
import os
import threading
import multiprocessing as mp

# cpu waster function
def cpu_waster():
    while True:
        pass

print('Hi my name is,',__name__)
if __name__ == '__main__':
    # process information
    print('\n Process ID:', os.getpid())
    print('\nThread Count:', threading.active_count())
    for thread in threading.enumerate():
        print(thread)

    print('Starting 3 CPU wasters..')
    for i in range(3):
        mp.Process(target=cpu_waster).start()

        # display information about this process
        print('\n Process ID:', os.getpid())
        print('\nThread Count:', threading.active_count())


