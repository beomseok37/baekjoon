n,k=list(map(int,input().split()))
coin = [int(input()) for _ in range(n)]
dp=[0 for _ in range(k+1)]

for i in range(k+1):
    for j in range(n):
        if i-coin[j]<0:
            continue
        
        if i-coin[j]!=0 and dp[i-coin[j]]==0:
            continue
        
        if dp[i]==0:
            dp[i]=dp[i-coin[j]]+1
        else:
            dp[i]=min(dp[i],dp[i-coin[j]]+1)

print(dp[k] if dp[k]!=0 else -1)
