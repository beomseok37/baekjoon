n,k=list(map(int,input().split()))
kinds=[int(input()) for _ in range(n)]
dp=[0 for _ in range(k+1)]
dp[0]=1
for i in range(n):
    for j in range(1,k+1):
        if j-kinds[i]>=0:
            dp[j]=dp[j]+dp[j-kinds[i]]
print(dp[k])
