from pathlib import Path
import sys

def inputF():
    original_stdin=sys.stdin
    timingInputs=[]
    with open(Path(__file__).parent/'priority-Process-Scheduling-Input.txt','r') as f:
        sys.stdin=f
        numProcess=int(input())
        for i in range(numProcess):
            processIds,arrivalTimes,burstTimes,priority=input().split()
            arrivalTimes,burstTimes,priority=map(int,(arrivalTimes,burstTimes,priority))
            temp=[processIds,arrivalTimes,burstTimes,priority]
            timingInputs.append(temp)
    timingInputs=sorted(timingInputs,key=lambda x:x[1])
    sys.stdin=original_stdin

    return numProcess,timingInputs


def timings(numProcess,timingsInputs):
    completeTimes=[0]*numProcess
    waitingTimes=[timingsInputs[i][2] for i in range(numProcess)]
    turnTimes=[0]*numProcess
    currentTime=1
    gantt_chart=''
    while True:
        done=[timingsInputs[i][2]<=0 for i in range(numProcess)]  
        if all(done):  
            break
        ind=-1
        highestPriority=-1   
        for j in range(numProcess):
       
            if currentTime>=timingsInputs[j][1]:
                if timingsInputs[j][3]>highestPriority:
                    if timingsInputs[j][2]>0:
                        highestPriority=timingsInputs[j][3]
                        ind=j
        currentTime+=1
        if ind==-1:
            gantt_chart+='|  '
            continue
        timingsInputs[ind][2]-=1
        if timingsInputs[ind][2]<=0:
            completeTimes[ind]=currentTime
        gantt_chart+=f'| {timingsInputs[ind][0]}'


    for j in range(numProcess):
        turnTimes[j]=completeTimes[j]-timingsInputs[j][1]
        waitingTimes[j]=turnTimes[j]-waitingTimes[j]
    print(gantt_chart)
    totalTurn,totalWait=sum(turnTimes),sum(waitingTimes)


    for i in range(numProcess):
        print('Process:',timingsInputs[i][0],',completion time:',completeTimes[i],',waiting time:',waitingTimes[i],',turn around time:',turnTimes[i])
    print('Average waiting time:',totalWait/numProcess,'Average turn around time:',totalTurn/numProcess)


def main():
    numProcess,timingsInputs=inputF()
    timings(numProcess,timingsInputs)

if __name__=='__main__':
    main()