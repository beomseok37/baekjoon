N=int(input())
A=list(map(int,input().split()))
dp=[0 for _ in range(N)]
dp[0]=A[0]
answer=A[0]

for i in range(1,N):
    dp[i]=A[i]+max(dp[i-1],A[i-1])
    answer=max(answer,dp[i],A[i])

print(answer)
