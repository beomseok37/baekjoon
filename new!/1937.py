import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def recursion(x,y):
    global n
    
    if dp[x][y]!=1:
        return dp[x][y]
    
    maxMove=1
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        
        if not (0<=nx<n and 0<=ny<n) or bamboo[nx][ny]<=bamboo[x][y]:
            continue
        
        maxMove=max(maxMove,1+recursion(nx,ny))
    
    dp[x][y]=maxMove
    return dp[x][y]
        
n=int(input())
bamboo=[list(map(int,input().split())) for _ in range(n)]
dp=[[1 for _ in range(n)] for __ in range(n)]
dx,dy=[-1,1,0,0],[0,0,1,-1]
answer = 0
for i in range(n):
    for j in range(n):
        answer=max(answer,recursion(i,j))
print(answer)
