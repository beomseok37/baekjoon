import sys
input = sys.stdin.readline
def dfs(i,j):
    global M,N
    if i==M-1 and j==N-1:
        return 1
    
    if dp[i][j]!=-1:
        return dp[i][j]
    
    dp[i][j]=0
    for k in range(4):
        nx,ny=i+mx[k],j+my[k]
        if 0<=nx<M and 0<=ny<N and board[i][j]>board[nx][ny]:
            dp[i][j]+=dfs(nx,ny)
            
    return dp[i][j]

M,N=list(map(int,input().split()))
board=[list(map(int,input().split())) for _ in range(M)]
dp=[[-1 for _ in range(N)] for __ in range(M)]
mx=[0,0,-1,1]
my=[1,-1,0,0]
print(dfs(0,0))
