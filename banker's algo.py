
"""
Hrithik
banker algorithm


"""


import numpy as np
def Data():
    try:
        Processes=int(input("Enter the number of processes :"))
        Resources=int(input("Enter the number of resources :"))
        alloc = np.zeros((Processes,Resources))
        max = np.zeros((Processes,Resources))
        print("\n For Allocation Resources Matrix")
        for i in range(Processes):
            alloc[i] = np.array([int(i)
            for i in input(f"Enter Allocated resources for process P{i+1}: \t").split()])
        print("\n For Maximum Resources Matrix")
        for i in range(Processes):
            max[i] = np.array([int(i) 
            for i in input(f"Enter Maximum resources for process P{i+1}: \t").split()])
        avail = np.array([int(i) 
        for i in input("Now enter the values of the available resources: \t\t").split()])
    except:
        print("incorrect values entered try again.")    
    return alloc, max, avail

def Algo(alloc, need, avail):
    n,m = alloc.shape
    work = avail
    finish = np.zeros(n)
    sequence = []
    while 1:
        retry = 0
        for i in range(n):
            compare = need[i] <= work
            if finish[i] == 0 and compare.all():
                work = work + alloc[i]
                finish[i] = 1
                sequence.append(i)
                retry = 1
                print(f"\n Available matrix after {i+1} process = \n", work)
        if not retry:   
            break
    for i in finish:
        if not i:   
            return 0, 0
    return 1, work, sequence

alloc, max, avail, total = Data()
need = max - alloc
answer, work, sequence = Algo(alloc, need, avail)
print("\n Need matrix = \n", need)
out = "Yes, safe state" if answer else "No, unsafe state."
print(work)
print(out)
if sequence:   print("" + "".join((["P" + str(i) + "-> " for i in sequence])).rstrip())