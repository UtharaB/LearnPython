# Code to understand threading
import os
import threading

# cpu waster function
def cpu_waster():
    while True:
        pass

# process information
print('\n Process ID:', os.getpid())
print('\nThread Count:', threading.active_count())
for thread in threading.enumerate():
    print(thread)

print('Starting 12 CPU wasters..')
for i in range(12):
    threading.Thread(target=cpu_waster).start()

    # display information about this process
    print('\n Process ID:', os.getpid())
    print('\nThread Count:', threading.active_count())
    for thread in threading.enumerate():
        print(thread)

