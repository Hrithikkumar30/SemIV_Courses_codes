#Author :- Hrithik - Kumar

              #Date :- 24 Feb 2022

#Time :- 09:10 p.m.
Process_array = []
Burst_Time = []
Arrival_Time = []
Gantt_Chart = []
n = int(input("Enter the number of Processes"))
for i in range(n):
    Process_id = 'P' + str(input("Enter the Process Number"))
    b = Process_array.extend([Process_id])
    print("Process Number",Process_array)
    
for j in range(n):
    x = int(input("Enter the Burst Times"))
    c = Burst_Time.extend([x])
    print("Burst Time",Burst_Time)

for k in range(n):
    b = int(input("Enter the arrival times"))
    c = Arrival_Time.extend([b])
    print("Arrival Time",Arrival_Time)

order1 = Burst_Time.sort()
order2 = Arrival_Time.sort()

Arrange = print("Sorted Burst Time",Burst_Time)
Assign = print("Sorted Arrvial Time",Arrival_Time)

New_Burst_Time = []
for j in range(-n,0):
    a = Burst_Time[j]
    New_Burst_Time.extend([a])
    print("New_Burst_Time",New_Burst_Time)

add = 0
Gantt_Chart = []
for k in range(0,n):
    add = add + New_Burst_Time[k]
    a = Gantt_Chart.append(add)
    print("Gantt Chart",Gantt_Chart)

New_Arrvial_Time = []
for k in range(-n,0):
    b = Arrival_Time[k]
    New_Arrvial_Time.extend([b])
    print("New Arrival Time",New_Arrvial_Time)

TAT = []
for j in range(n):
    Subtract = Gantt_Chart[j] - New_Arrvial_Time[k]
    b = TAT.append(Subtract)
    print("TAT ",TAT)

WT = []
for n in range(0,n):
    Subtract = TAT[n] - New_Burst_Time[n]
    c = WT.append(Subtract)
    print("WT ",WT)

RD = []
for  i in range(n):
    Subtract = TAT[i] / New_Burst_Time[i]
    c = RD.append(Subtract)
    print("RD ",RD)
avg_wt = 0
for i in WT:
    avg_wt += i
avg_wt = (avg_wt/n)
print("Average Waiting Time",avg_wt)







    


    

    
    
    
  
    
    
    


        
