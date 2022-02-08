import math
numofthing=int(input())
thinglist=[]
for i in range(numofthing):
    thing=input()
    thinglist.append(thing.split())

for i in range(numofthing):
    numlist=thinglist[i]
    for i in range(len(numlist)):
        numlist[i]=float(numlist[i])
    x1=numlist[0]
    y1=numlist[1]
    r1=numlist[2]
    x2=numlist[3]
    y2=numlist[4]
    r2=numlist[5]
    distance=math.sqrt((x1-x2)**2+(y1-y2)**2)
    if x1==x2 and y1==y2 and r1==r2:
        print(-1)
    else:
        if distance==r1+r2 or distance==abs(r1-r2):
            print(1)
        elif distance<r1+r2 and distance>abs(r1-r2):
            print(2)
        else:
            print(0)
        