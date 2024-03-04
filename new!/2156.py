N = int(input())
graphs = [int(input()) for _ in range(N)]
dp = [[0, 0, 0] for _ in range(N)]
# 0-> 1연속인 잔에 마셨을 경우, 2연속인 잔에 마셨을 경우 ...
dp[0][1] = graphs[0]
for i in range(1, N):
    dp[i][0] = max(dp[i-1])
    dp[i][1] = dp[i-1][0]+graphs[i]
    dp[i][2] = dp[i-1][1]+graphs[i]
print(max(dp[N-1]))
