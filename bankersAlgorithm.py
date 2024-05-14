def bankers(allocated,maxed,available):
    nP=len(allocated)
    nK=len(allocated[0])
    needed=[[maxed[i][j]-allocated[i][j] for j in range(nK)] for i in range(nP)]
    safe=[]
    queue=[i for i in range(nP)]
    while len(queue)>0:
        flag=True
        for j in range(nK):
            if needed[queue[0]][j]>available[j]:
                flag=False
                break
        if flag is True:
            safe.append(queue[0]+1)
            for j in range(nK):
                available[j]+=allocated[queue[0]][j]
            queue.pop(0)
        else:
            temp=queue[0]
            queue.pop(0)
            queue.append(temp)
    for c in safe:
        print(f'P{c}')

def main():
    allocated=[
        [0,1,0],
        [2,0,0],
        [3,0,2],
        [2,1,1],
        [0,0,2]
    ]
    maxed=[
        [7,5,3],
        [3,2,2],
        [9,0,2],
        [2,2,2],
        [4,3,3]
    ]
    available=[3,3,2]
    bankers(allocated,maxed,available)
    
if __name__=='__main__':
    main()