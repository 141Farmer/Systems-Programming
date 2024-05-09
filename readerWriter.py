from time import sleep
import threading

resource=''
readers=0
mutex=threading.Lock()
readerSem=threading.Semaphore(1)
writerSem=threading.Semaphore(1)

def read(readerId):
    global readers,resource
    readerSem.acquire()
    mutex.acquire()
    readers+=1
    readerSem.release()
    print(f'Reader {readerId} is reading {resource}')
    readers-=1
    if readers==0:
        writerSem.release()
    mutex.release()

def readerThread(readerId):
    while True:
        read(readerId)
        sleep(1)

def write(writerId,value):
    global resource
    mutex.acquire()
    writerSem.acquire()
    print(f'Writer {writerId} is writing {value}')
    resource+=value
    writerSem.release()
    mutex.release()

def writerThread(writerId,value):
    while True:
        write(writerId,value)
        sleep(2)

def main():
    readerThreads=[]
    for i in range(3):
        t=threading.Thread(target=readerThread,args=(i+1,))
        t.start()
        readerThreads.append(t)

    writerThreads=[]
    for i in range(3):
        t=threading.Thread(target=writerThread,args=(i+1,chr(ord('a')+i)))
        t.start()
        writerThreads.append(t)

    for t in readerThreads:
        t.join()

    for t in writerThreads:
        t.join()

if __name__=='__main__':
    main()