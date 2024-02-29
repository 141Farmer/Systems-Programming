from pathlib import Path
import sys

def inputF():
    original_stdin=sys.stdin
    timingInputs=[]
    with open(Path(__file__,).resolve().parent/'priority-Process-Scheduling-Input.txt','r') as f:
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

def prioritySort(numProcess,timingsInputs):
    current=timingsInputs[0][2]
    for i in range(1,numProcess):
        idx=i
        if current>=timingsInputs[i][1]:
            for j in range(i+1,numProcess): 
                if timingsInputs[j][3]>timingsInputs[idx][3]:
                    idx=j
        timingsInputs[i],timingsInputs[idx]=timingsInputs[idx],timingsInputs[i]
        current+=timingsInputs[i][2]

def timings(numProcess,timingsInputs):
    startTimes=[0]*numProcess
    completeTimes=[timingsInputs[0][1]+timingsInputs[0][2]]*numProcess
    completeTimes=[timingsInputs[0][1]+timingsInputs[0][2]]*numProcess
    waitingTimes=[0]*numProcess
    turnTimes=[completeTimes[0]-timingsInputs[0][1]]*numProcess

    totalTurn,totalWait=0,0

    for i in range(1,numProcess):
        startTimes[i]=max(completeTimes[i-1],timingsInputs[i][1])
        completeTimes[i]=startTimes[i]+timingsInputs[i][2]
        waitingTimes[i]=max(0,completeTimes[i-1]-timingsInputs[i][1])
        turnTimes[i]=completeTimes[i]-timingsInputs[i][1]
        totalWait+=waitingTimes[i]
        totalTurn+=turnTimes[i]
    
    print("Gantt Chart:")
    timeline=""
    for i in range(numProcess):
        timeline+="|"
        timeline+=" "*(startTimes[i]-len(timeline))  
        timeline+=(timingsInputs[i][0]+' ')*(completeTimes[i]-startTimes[i])  # Process ID
    timeline+="|"
    print(timeline,'\n')

    for i in range(numProcess):
        print('Process:',timingsInputs[i][0],',starting time:',startTimes[i],',completion time:',completeTimes[i],',waiting time:',waitingTimes[i],',turn around time:',turnTimes[i])
    print('Average waiting time:',totalWait/numProcess,'Average turn around time:',totalTurn/numProcess)

def main():
    numProcess,timingsInputs=inputF()
    prioritySort(numProcess,timingsInputs)
    timings(numProcess,timingsInputs)

if __name__=='__main__':
    main()