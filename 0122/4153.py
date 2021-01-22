while True:
    thinginput=input()
    thinglist=thinginput.split()
    side=[]
    for i in range(len(thinglist)):
        side.append(int(thinglist[i]))
    if 0 in side:
        break
    side.sort()
    if side[2]**2==side[1]**2+side[0]**2:
        print("right")
    else:
        print("wrong")
