N=int(input())
A=[int(input()) for _ in range(N)]
dp=[[0,0] for _ in range(N)]
dp[0][0],dp[0][1]=A[0],A[0]

if N!=1:
    dp[1][0],dp[1][1]=A[1],A[0]+A[1]
    
for i in range(2,N):
    dp[i][0]=max(dp[i-2][0],dp[i-2][1])+A[i]
    dp[i][1]=dp[i-1][0]+A[i]

print(max(dp[N-1]))
