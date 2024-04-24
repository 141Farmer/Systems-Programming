mutex=1
full=0
empty=5
item=0

def producer():
    global mutex,full,empty,item
    mutex-=1
    full+=1
    empty-=1
    item+=1
    print(f'Produced item {item}')
    mutex+=1

def consumer():
    global mutex,full,empty,item
    mutex-=1
    full-=1
    empty+=1
    print(f'Consumed item {item}')
    item-=1
    mutex+=1

def main():
    print('P. Produce\nC. Consume\nE. Exit')
    while True:
        print('Option')
        n=input()
        if n=='P':
            if mutex==1 and empty!=0:
                producer()
            else:
                print('Buffer is full')
        elif n=='C':
            if mutex==1 and full!=0:
                consumer()
            else:
                print('Buffer is empty')
        else:
            return 
        
if __name__=='__main__':
    main()