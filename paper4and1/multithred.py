'''Q13. Give a real time example for multithreading. Is it a good idea to use multi-thread to
speed your Python code?'''

import time
import threading

def print_numbers():
    for i in range(1, 11):
        print('thread 1->',i)
        time.sleep(1)
def print_letters():
    for letter in ['a', 'b', 'c', 'd', 'e']:
        print('thread 2 ->',letter)
        time.sleep(1)
# Create two threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

# Start the threads
t1.start()

t2.start()

# Wait for the threads to finish
t1.join()
t2.join()

print("Done")