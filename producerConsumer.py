from threading import Thread,Semaphore,Lock
from time import sleep

mutex=Lock()
empty=Semaphore(5)
full=Semaphore(1)
num_items=0
max_num_items=5
max_num_consumers=8

def producer():
    global num_items
    while True:
        empty.acquire()
        mutex.acquire()
        num_items+=1
        print(f'Produced item {num_items}')
        mutex.release()
        full.release()
        sleep(1)
        
def consumer(consumer_num):
    global num_items
    while True:
        full.acquire()
        mutex.acquire()
        print(f'Consumer {consumer_num} consumed item {num_items}')
        num_items-=1
        mutex.release()
        empty.release()
        sleep(1)

def main():
    for i in range(max_num_items):
        Thread(target=producer).start()
    for i in range(max_num_consumers):
        Thread(target=consumer,args=(i+1,)).start()

if __name__=='__main__':
    main()