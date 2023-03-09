import sys
input = sys.stdin.readline

def find1(s,num):
    global N
    e=N-1
    while s<=e:
        m=(s+e)//2
        if prefix[m]==num:
            return m
        elif prefix[m]>num:
            e=m-1
        else:
            s=m+1
    return m if prefix[m]>num else m+1

def find2(s,num):
    global N
    e=N-1
    while s<=e:
        m=(s+e)//2
        if prefix[m]==num:
            return m
        elif prefix[m]>num:
            e=m-1
        else:
            s=m+1
    return m+1 if prefix[m]<num else m

N=int(input())
A=list(map(int,input().split()))
result=0

A.reverse()
prefix = [A[0]]
for a in range(1,N):
    prefix.append(prefix[-1]+A[a])
x,y=0,1
while True:
    stomach=prefix[x]
    y=find1(y,stomach*2+1)
    if y>N-2:
        break
    temp=find2(y,prefix[N-1]-stomach+1)
    result+=N-temp-1
    
    x+=1
    
print(result)
