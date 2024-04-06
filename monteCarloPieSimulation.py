from random import randrange

def simulate():
    citr=0
    itr=10**6
    for i in range(itr):
        x=randrange(-1,1)
        y=randrange(-1,1)
        if (x**2+y**2)<=1:
            citr+=1
    pie=(citr/itr)*4
    print(pie)

def main():
    simulate()

if __name__=='__main__':
    main()
