N, K = list(map(int, input().split()))
dp = [[0 for __ in range(201)] for _ in range(201)]

for i in range(201):
    dp[1][i] = i
    dp[i][2] = i+1
    dp[i][1] = 1

for i in range(2, 201):
    for j in range(2, 201):
        dp[i][j] = (dp[i][j-1]+dp[i-1][j]) % 1_000_000_000
print(dp[N][K])
