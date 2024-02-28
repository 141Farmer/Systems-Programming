from pathlib import Path
import sys

def inputF():
    original_stdin=sys.stdin
    with open(Path(__file__,).resolve().parent/'non-Priority-Process-Scheduling-Input.txt','r') as f:
        sys.stdin=f
        numProcess=int(input())
        processIds=[None]*(numProcess)
        arrivalTimes=[None]*(numProcess)
        burstTimes=[None]*(numProcess)
        for i in range(numProcess):
            processIds[i],arrivalTimes[i],burstTimes[i]=input().split()
            arrivalTimes[i],burstTimes[i]=map(int,(arrivalTimes[i],burstTimes[i]))
    sys.stdin=original_stdin
    return numProcess,processIds,arrivalTimes,burstTimes


def timings(numProcess,processIds,arrivalTimes,burstTimes):
    startTimes=[0]*numProcess
    completeTimes=[arrivalTimes[0]+burstTimes[0]]*numProcess
    waitingTimes=[0]*numProcess
    turnTimes=[completeTimes[0]-arrivalTimes[0]]*numProcess

    totalTurn,totalWait=0,0

    for i in range(1,numProcess):
        startTimes[i]=max(completeTimes[i-1],arrivalTimes[i])
        completeTimes[i]=startTimes[i]+burstTimes[i]
        waitingTimes[i]=max(0,completeTimes[i-1]-arrivalTimes[i])
        turnTimes[i]=completeTimes[i]-arrivalTimes[i]
        totalWait+=waitingTimes[i]
        totalTurn+=turnTimes[i]

    for i in range(numProcess):
        print('Process ',processIds[i],', starting time: ',startTimes[i],', completion time: ',completeTimes[i],', waiting time: ',waitingTimes[i],', turn around time: ',turnTimes[i])

    print('Average waiting time:',totalWait/numProcess,'Average turn around time:',totalTurn/numProcess)

def main():
    numProcess,processIds,arrivalTimes,burstTimes=inputF()
    timings(numProcess,processIds,arrivalTimes,burstTimes)

if __name__=='__main__':
    main()