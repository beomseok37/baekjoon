def rotate(t_top,d):
    if d==1:
        temp=[0 for _ in range(8)]
        for i in range(1,8):
            temp[i]=t_top[i-1]
        temp[0]=t_top[7]
    else:
        temp=[0 for _ in range(8)]
        for i in range(7):
            temp[i]=t_top[i+1]
        temp[7]=t_top[0]    
    return temp

top=[list(input()) for _ in range(4)]
k=int(input())
rotates=[list(map(int,input().split())) for _ in range(k)]
result=0
for which,direction in rotates:
    array=[]
    if which==1:
        array.append([0,direction])
        if top[0][2]!=top[1][6]:
            array.append([1,-direction])
            if top[1][2]!=top[2][6]:
                array.append([2,direction])
                if top[2][2]!=top[3][6]:
                    array.append([3,-direction])
    elif which==2:
        array.append([1,direction])
        if top[0][2]!=top[1][6]:
            array.append([0,-direction])
        if top[1][2]!=top[2][6]:
            array.append([2,-direction])
            if top[2][2]!=top[3][6]:
                array.append([3,direction])
    elif which==3:
        array.append([2,direction])
        if top[2][2]!=top[3][6]:
            array.append([3,-direction])
        if top[1][2]!=top[2][6]:
            array.append([1,-direction])
            if top[0][2]!=top[1][6]:
                array.append([0,direction])
    else:
        array.append([3,direction])
        if top[2][2]!=top[3][6]:
            array.append([2,-direction])
            if top[1][2]!=top[2][6]:
                array.append([1,direction])
                if top[0][2]!=top[1][6]:
                    array.append([0,-direction])

    for w,d in array:
        top[w]=rotate(top[w][:],d)

for i in range(4):
    result+=2**i if top[i][0]=='1' else 0
print(result)
