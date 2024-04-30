import signal
import threading
import time
import sys

def thread_task():
    while True:
        print("Thread task is running...")
        time.sleep(1)

def sigint_handler(signum, frame):
    print("\nSIGINT signal caught. Terminating program.")
    sys.exit(0)

def main():
    signal.signal(signal.SIGINT,sigint_handler)

    thread=threading.Thread(target=thread_task)
    #thread.daemon=True  
    thread.start()

    while True:
        print("Main program is running...")
        time.sleep(1)

if __name__ == "__main__":
    main()
