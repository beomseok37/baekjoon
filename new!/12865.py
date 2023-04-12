N,K=list(map(int,input().split()))
W,V=[0],[0]
dp=[[0 for _ in range(N+1)] for _ in range(K+1)]
result=0
for i in range(N):
    w,v=list(map(int,input().split()))
    W.append(w)
    V.append(v)

for i in range(N):
    dp[0][i]=0
    
for i in range(K+1):
    for j in range(1,N+1):
        if W[j]>i:
            dp[i][j]=dp[i][j-1]
        else:
            dp[i][j]=max(dp[i][j-1],dp[i-W[j]][j-1]+V[j])
print(dp[K][N])
