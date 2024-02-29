from pathlib import Path
import sys

def inputF():
    original_stdin=sys.stdin
    timingInputs=[]
    with open(Path(__file__).parent/'non-Priority-Process-Scheduling-Input.txt','r') as f:
        sys.stdin=f
        numProcess,quantam=map(int,input().split())
        for i in range(numProcess):
            processIds,arrivalTimes,burstTimes=input().split()
            arrivalTimes,burstTimes=map(int,(arrivalTimes,burstTimes))
            temp=[processIds,arrivalTimes,burstTimes]
            timingInputs.append(temp)
    timingInputs=sorted(timingInputs,key=lambda x:x[1])
    sys.stdin=original_stdin
    return numProcess,timingInputs,quantam

def timings(numProcess,timingsInputs,quantam):
    completeTimes=[0]*numProcess
    waitingTimes=[timingsInputs[i][2] for i in range(numProcess)]
    turnTimes=[0]*numProcess
    currentTime=1
    gantt_chart=''
    while True:
        done=[timingsInputs[i][2]<=0 for i in range(numProcess)]  
        if all(done):  
            break

        noProcess=True
        for j in range(numProcess):
            cpuTime=0
            if currentTime>=timingsInputs[j][1] and timingsInputs[j][2]>0:
                noProcess=False
                if timingsInputs[j][2]<=quantam:
                    cpuTime=timingsInputs[j][2]
                    timingsInputs[j][2]-=cpuTime
                    gantt_chart+=(''.join(f'|{timingsInputs[j][0]}' for _ in range(cpuTime)))
                else:
                    cpuTime=quantam
                    timingsInputs[j][2]-=cpuTime
                    gantt_chart+=(''.join(f'|{timingsInputs[j][0]}' for _ in range(cpuTime)))
                #print(timingsInputs[j][0],currentTime)
                completeTimes[j]=currentTime
                currentTime+=cpuTime
        if noProcess is True:
            currentTime+=1
        

    for j in range(numProcess):
        turnTimes[j]=completeTimes[j]-timingsInputs[j][1]
        waitingTimes[j]=turnTimes[j]-waitingTimes[j]
    print(gantt_chart)
    totalTurn,totalWait=sum(turnTimes),sum(waitingTimes)


    for i in range(numProcess):
        print('Process:',timingsInputs[i][0],',completion time:',completeTimes[i],',waiting time:',waitingTimes[i],',turn around time:',turnTimes[i])
    print('Average waiting time:',totalWait/numProcess,'Average turn around time:',totalTurn/numProcess)

def main():
    numProcess,timingsInputs,quantam=inputF()
    timings(numProcess,timingsInputs,quantam)

if __name__=='__main__':
    main()