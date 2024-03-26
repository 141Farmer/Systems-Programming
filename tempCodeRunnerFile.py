print("Gantt Chart:")
    timeline=""
    for i in range(numProcess):
        timeline+="|"
        timeline+=" "*(startTimes[i]-len(timeline))  
        timeline+=(timingsInputs[i][0]+' ')*(completeTimes[i]-startTimes[i])  # Process ID
    timeline+="|"
    print(timeline)