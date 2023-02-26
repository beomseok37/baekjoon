import sys
input = sys.stdin.readline

def find_next_one(now):
    global N
    i=now
    for i in range(now,N+1):
        if B[i]==1:
            break
    return i

N,M=list(map(int,input().split()))
B=[0]+list(map(int,input().split()))
A=[0 for _ in range(N+1)]
used=[False for _ in range(N+1)]
for i in range(M):
    index,number = list(map(int,input().split()))
    A[index]=number
    used[number] = True

one_index=find_next_one(1)
now=1
while one_index<N+1:
    value=one_index
    temp=now
    while now<=one_index:
        if value<temp:
            print(-1)
            exit()
            
        if A[now]==0:
            if not used[value]:
                A[now]= value
                used[value]=True
                now+=1
                value-=1
            else:
                value-=1
        elif temp<=A[now]<=one_index:
            now+=1
        else:
            print(-1)
            exit()
        
    one_index = find_next_one(one_index+1)

print(' '.join(map(str,A[1:])))
