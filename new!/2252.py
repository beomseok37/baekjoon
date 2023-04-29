import sys
input = sys.stdin.readline

N,M=list(map(int,input().split()))
followed = [[] for _ in range(N+1)]
isFollowing = [0 for _ in range(N+1)]
visited = [False for _ in range(N+1)]
result=[]

for _ in range(M):
    a,b=list(map(int,input().split()))
    followed[a].append(b)
    isFollowing[b]+=1
    
for i in range(1,N+1):
    if visited[i]:
        continue
    
    if not followed[i] and isFollowing[i]==0:
        result.append(i)
        continue
    
    if not (followed[i] and isFollowing[i]==0):
        continue
    
    visited[i]=True
    result.append(i)
    stack=[i]
    while stack:
        num = stack.pop()
        
        for nextNum in followed[num]:
            if visited[nextNum]:
                continue
            
            isFollowing[nextNum]-=1
            if isFollowing[nextNum]==0:
                visited[nextNum]=True
                stack.append(nextNum)
                result.append(nextNum)
print(' '.join(map(str,result)))
