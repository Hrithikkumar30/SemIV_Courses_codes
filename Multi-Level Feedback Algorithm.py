#Hrithik kumar
#Enrollment Number - BT20HCS199
#Multi - Level Feedback Scheduling Algorithm
#Starting with the code

#Input for Process ID's 
from prettytable import PrettyTable
import pandas as pd
Process_ID = []
n = int(input("Enter the Number of Processes you want"))
for i in range(n):
    c = 'P' + str(input("Enter the Process ID"))
    Process_ID.append(c)
print("The Process ID's ",Process_ID)

#Input for Burst Times
Burst_Time = []
for j in range(n):
    c = int(input("Enter the Burst Times Respectively for each Processes"))
    Burst_Time.append(c)
print("The Burst Times",Burst_Time)

#Input for Arrival Times
Arrival_Time = []
for k in range(n):
    c = int(input("Enter the Arrival Times Respectively for each Processes"))
    Arrival_Time.append(c)
print("The Arrival Times",Arrival_Time)

#Relating each inputs with the Process ID's
#Relating Process ID's with the Burst Times through dictionary
keys_List = Process_ID
values_List = Burst_Time
dictionary1 = dict(zip(keys_List,values_List))
x1 = list(dictionary1.keys())
y1 = list(dictionary1.values())

#Relating Process ID's with Arrival Times through Dictionaries
Process_List = Process_ID
Arrival_List = Arrival_Time
dictionary2 = dict(zip(Process_List,Arrival_List))
x2 = list(dictionary2.keys())
y2 = list(dictionary2.values())

#Code for Relating Burst Times with Arrival Times
Burst_List = Burst_Time
Arrival_List = Arrival_Time
dictionary3 = dict(zip(Burst_List,Arrival_List))
x3 = list(dictionary3.keys())
y3 = list(dictionary3.values())

#Queue and Queue Number along with Quantum ID
imp = int(input("Enter the Quantum Number for all the Process"))
x = int(input("Enter the Number of Queues you want"))
Queue_ID = []
for i in range(x):
    c = 'Q' + str(input("Enter the Queue ID"))
    Queue_ID.append(c)
    
#Code for appending Quantum Number in each Queue
Quantum_Num = []
for k in range(x):
    print("Enter Quantum Number for",Queue_ID[k])
    print("If Queue falls in FCFS just Type 0")
    q = int(input())
    Quantum_Num.append(q)

#Code for Relating Quantum Number with Queue_ID
Queue_List = Queue_ID
Quantum_List = Quantum_Num
dictionary4 = dict(zip(Queue_List,Quantum_List))
x4 = list(dictionary4.keys())
y4 = list(dictionary4.values())

print("The Queue for FCFS Scheduling Algorithm is")
print(x4[-1])
y4[-1] = 0               
#Database System (All Datas Included)
#All Key Datas
Register1 = []
Register1.extend([x1])
Register2 = []
Register2.extend([x2])
Register3 = []
Register3.extend([x3])
Register4 = []
Register4.extend([x4])

#All Value Data
Directory1 = []
Directory1.extend([y1])
Directory2 = []
Directory2.extend([y2])
Directory3 = []
Directory3.extend([y3])
Directory4 = []
Directory4.extend([y4])

#Gantt Chart Code
#Starting with First Process in the list
Pre_Gantt_Chart = []
count = 0
add = 0
for i in range(x-1):
    count = count + y4[i]
    sub = y1[i] - count
    Pre_Gantt_Chart.append(count)
    print(Pre_Gantt_Chart)
for j in range(1):
    sub = y1[0] - Pre_Gantt_Chart[1]
    add = sub + Pre_Gantt_Chart[1]
    Pre_Gantt_Chart.append(add)
    print(Pre_Gantt_Chart)
       
#Starting with the Remaining Process
Ready_Queue = []
count = 0
add = 0
for k in range(x-1):
    if Pre_Gantt_Chart[2] > y1[1] and Pre_Gantt_Chart[2] > y1[2]:
        Ready_Queue.extend([x1[1],x1[2]])
        print("The Current Ready Queue is ",Ready_Queue)
    else:
        print("Enter all the values from the start again")
#Rest Remaining Processes
for m in range(x-1):
    sub = y1[m+1] - y4[0]
    c = Pre_Gantt_Chart[-1] + sub
    Pre_Gantt_Chart.append(c)
Pre_Gantt_Chart[3] = Pre_Gantt_Chart[3] - 4
print(Pre_Gantt_Chart)
 
#Left Over Burst Times to Get appended in Gantt Chart
count = 0
a = 1
for g in range(x-1):
    sub = y1[a] - y4[0]
    add = sub + Pre_Gantt_Chart[-1]
    Pre_Gantt_Chart.append(add)
    print("The Gantt Chart of MLFQS is",Pre_Gantt_Chart)
    a = a + 1
print("+------------+----------+--------------+-----------+-------------+--------------+")
#Code for Entering the Maximum Time of the Process ID
Max_Gantt = []
for i in range(n):
    print("Enter the Max Number in the Gantt Chart for Process ")
    print(Process_ID[i])
    c = int(input())
    Max_Gantt.append(c)
    
#Data Register for TAT (Turn Around Time) and Arrival Time
New_Process_list = Process_ID
New_Gantt_list = Max_Gantt
dictionary5 = dict(zip(New_Process_list,New_Gantt_list))
x5 = list(dictionary5.keys())
y5 = list(dictionary5.values())

#New Register
Register5 = []
Register5.extend([x5])

#New Directory
Directory5 = []
Directory5.extend([y5])

#Connecting Max Gantt Chart with the Arrival Time
Max_List = Max_Gantt
New_Arrival = Arrival_Time
dictionary6 = dict(zip(Max_List,New_Arrival))
x6 = list(dictionary6.keys())
y6 = list(dictionary6.values())

#New Arrival Register
Register6 = []
Register6.extend([x6])

#New Arrival Directory
Directory6 = []
Directory6.extend([y6])

#By First Come First Serve
#TAT = Turn Around Time
#TAT = The Last Completion Time - Arrival Time
TAT = []
for k in range(0,n):
    sub = x6[k] - y6[k]
    TAT.append(sub)
    
#Code for WT
#WT = TAT - Burst Time
#WT = Waiting Time
WT = []

for f in range(0,n):
    sub = TAT[f] - Burst_Time[f]
    WT.extend([sub])

#Code for RD
#RD = TAT / Burst Time
RD = []
for k in range(0,n):
    div = TAT[k] / Burst_Time[k]
    RD.extend([div])

#Code for Average Waiting Time (AVG WT)
avg_wt = 0
for i in WT:
    avg_wt += i
avg_wt = (avg_wt/n)
print("Average Waiting Time",avg_wt) 
   
#Tabular Representation
x = PrettyTable()
column_names = ['Burst Time','Arrival Time','Gantt Chart','TAT','WT','RD']
x.add_column(column_names[0],[Burst_Time])
x.add_column(column_names[1],[Arrival_Time])
x.add_column(column_names[2],[Pre_Gantt_Chart])
x.add_column(column_names[3],[TAT])
x.add_column(column_names[4],[WT])
x.add_column(column_names[5],[RD])

d = {
     'Process':[Process_ID]
    }
df = pd.DataFrame(data=d)
df
print(df)

print(x)
#Ending with the code