
#Author:Hrithik Kumar
#Enrollment Number - BT20HCS199
#Priority Scheduling (Non Preemptive)

import pandas as pd
n = int(input("Enter the number of Processes"))
Process_ID = []
for i in range(n):
    c = 'P' + str(input("Enter the Process ID"))
    Process_ID.append(c)
print(Process_ID)

class_list = dict()
print("Set the Priorities")
Priority_Process = []
count = 0
for j in range(n):
    count = count + 1
    print("Insert the Process for Priority Number ",count)
    key = count
    value = 'P' + str(input())
    print(value)
    Priority_Process.append(value)
    class_list[key] = [value]
print(Priority_Process)   
print("The Dict values are",class_list)

#Code for Priority Burst Times
Burst_Time = []
for i in range(n):
    c = int(input("Enter the Burst Times"))
    Burst_Time.append(c)
print(Burst_Time)

Burst_list = dict()
print("Enter Burst Times in order of the Priorities of the Processes")
Priority_Burst = []
for k in range(n):
    key = print(Priority_Process[k])
    value = int(input("Enter Burst Time"))
    Priority_Burst.extend([value])
    Burst_list[key] = [value]
print(Priority_Burst)

#Code for Priority Arrival Times
Arrival_Time = []
for i in range(n):
    c = int(input("Enter the Arrival Times"))
    Arrival_Time.append(c)

Arrival_list = dict()
print("Enter Arrival Times in order of Priorities of the Processes")
Priority_Arrival = []
for j in range(n):
    key = print(Priority_Process[j])
    value = int(input("Enter Arrival Time"))
    Priority_Arrival.extend([value])
    Arrival_list[key] = [value]
print(Priority_Arrival)

#Code for Gantt Chart
Gantt_Chart = []
add = 0
for k in range(n):
    add = add + Priority_Burst[k]
    Gantt_Chart.append(add)
print("Gantt Chart for Priority Scheduling ",Gantt_Chart)

#Code for  Turnaround Time

TAT = []
for b in range(0,n):
    sub = Gantt_Chart[b] - Priority_Arrival[b]
    TAT.append(sub)
    
#Code for Waiting Time
WT = []
for f in range(n):
    sub = TAT[f] - Priority_Burst[f]
    WT.append(sub)
    
#Code for RD

RD = []
for j in range(n):
    div = TAT[j] / Priority_Burst[j]
    RD.append(div)

#Code for Average Waiting Time 
avg_wt = 0
for i in WT:
    avg_wt += i
avg_wt = (avg_wt/n)
print("Average Waiting Time",avg_wt)    

#Code for Printing of the Table
d = {
     'Process':[Priority_Process],
     'Burst Time':[Priority_Burst],
     'Arrival Time':[Priority_Arrival],
     'Gantt Chart':[Gantt_Chart],
     'TAT':[TAT],
     'WT':[WT],
     'RD':[RD]
     }
df = pd.DataFrame(data=d)
df
print(df)

