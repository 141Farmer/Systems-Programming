import threading
import time

num_slices = 0
mutex = threading.Lock()
pizza = threading.Semaphore(0)
deliver = threading.Semaphore(1)

def student_thread(student_id):
    global num_slices
    while True:
        pizza.acquire()  
        mutex.acquire()
        if num_slices>0:
            num_slices-=1  
            print(f"Student {student_id} is eating pizza. Slices left: {num_slices}")
        else:
            print(f"Student {student_id} found no pizza. Going to sleep.")
            deliver.release()
            mutex.release()  
            pizza.acquire()  
            mutex.acquire()
            if num_slices>0:
                num_slices-=1  
                print(f"Student {student_id} is eating pizza. Slices left: {num_slices}")
            else:
                print(f"No pizza available even after delivery. Going to sleep.")
        mutex.release()
        time.sleep(1)


def delivery_thread():
    global num_slices
    while True:
        deliver.acquire()  
        mutex.acquire()
        if num_slices==0:
            num_slices+=8  
            print(f"Pizza delivered. Slices left: {num_slices}")
            mutex.release()
            for _ in range(num_students):  
                pizza.release()
        else:
            mutex.release()


num_students=10

student_threads=[]
for i in range(num_students):
    t=threading.Thread(target=student_thread,args=(i+1,))
    student_threads.append(t)
    t.start()

delivery_thread=threading.Thread(target=delivery_thread)
delivery_thread.start()

# Join threads
for t in student_threads:
    t.join()
delivery_thread.join()
