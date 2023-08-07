N=int(input())
fluid=list(map(int,input().split()))
fluid.sort()

if fluid[0]>0:
    print(fluid[0],fluid[1])
    exit()
elif fluid[-1]<0:
    print(fluid[-2],fluid[-1])
    exit()

minValue = 2_000_000_000
answer=[]
s,e=0,len(fluid)-1
while s<e:
    composite=fluid[s]+fluid[e]
    
    if minValue>abs(composite):
        minValue=abs(composite)
        answer=[fluid[s],fluid[e]]
    
    if composite<0:
        s+=1
    elif composite>0:
        e-=1
    else:
        break

print(answer[0],answer[1])
