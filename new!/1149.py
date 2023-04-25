import sys
input = sys.stdin.readline

N=int(input())
homes=[list(map(int,input().split())) for _ in range(N)]
dp=[homes[0][i] for i in range(3)]
for i in range(1,N):
    dp[0],dp[1],dp[2]=min(dp[1],dp[2])+homes[i][0],min(dp[0],dp[2])+homes[i][1],min(dp[0],dp[1])+homes[i][2]

print(min(min(dp[0],dp[1]),dp[2]))
