thinglist=[]
for i in range(3):
    x=input()
    xsplit=x.split()
    thinglist.append([int(xsplit[0]),int(xsplit[1])])

xdic={}
ydic={}
for i in range(3):
    if thinglist[i][0] in xdic.keys():
        xdic[thinglist[i][0]]+=1
    else:
        xdic[thinglist[i][0]]=1
    if thinglist[i][1] in ydic.keys():
        ydic[thinglist[i][1]]+=1
    else:
        ydic[thinglist[i][1]]=1
for key,value in xdic.items():
    if value==1:
        x=key
for key,value in ydic.items():
    if value==1:
        y=key
print(str(x)+" "+str(y))