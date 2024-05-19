from time import sleep
import threading

resource=''
readers=0
mutex=threading.Lock()
readerSem=threading.Semaphore(3)
writerSem=threading.Semaphore(1)

def readerThread(readerId):
    while True:
        global readers,resource
        readerSem.acquire()
        mutex.acquire()
        readers+=1
        if readers>0:
            writerSem.acquire()
        print(f'Reader {readerId} is reading {resource}')
        readerSem.release()
        mutex.release()
        mutex.acquire()
        readers-=1
        if readers==0:
            writerSem.release()
        mutex.release()
        sleep(2)

def writerThread(writerId,value):
    while True:
        global resource
        writerSem.acquire()
        print(f'Writer {writerId} is writing {value}')
        resource+=value
        writerSem.release()
        sleep(2)

def main():
    readerThreads=[]
    for i in range(3):
        t=threading.Thread(target=readerThread,args=(i+1,)).start()

    for i in range(3):
        threading.Thread(target=writerThread,args=(i+1,chr(ord('a')+i))).start()
        
if __name__=='__main__':
    main()