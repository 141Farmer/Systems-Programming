from threading import Thread, Semaphore, Lock
from time import sleep

mutex = Lock()
empty = Semaphore(5)  # Initially, all slots are empty
full = Semaphore(0)   # Initially, no items are produced
num_items = 0
max_num_items = 5
max_num_consumers = 8

def producer():
    global num_items
    while True:
        empty.acquire()   # Wait for an empty slot
        mutex.acquire()
        num_items += 1
        print(f'Produced item {num_items}')
        mutex.release()
        full.release()    # Signal that an item has been produced
        sleep(1)
        
def consumer(consumer_num):
    global num_items
    while True:
        full.acquire()    # Wait for an available item
        mutex.acquire()
        print(f'Consumer {consumer_num} consumed item {num_items}')
        num_items -= 1
        mutex.release()
        empty.release()   # Signal that a slot is now empty
        sleep(1)

def main():
    for i in range(max_num_consumers):
        Thread(target=consumer, args=(i+1,)).start()
    for i in range(max_num_items):
        Thread(target=producer).start()

if __name__ == '__main__':
    main()
