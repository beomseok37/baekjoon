thinginput=input()
thinglist=thinginput.split()
for i in range(len(thinglist)):
    thinglist[i]=int(thinglist[i])
x=thinglist[0]
y=thinglist[1]
thinglist[2]-=x
thinglist[3]-=y
thinglist.sort()
print(thinglist[0])