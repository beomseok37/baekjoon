N, M = list(map(int, input().split()))
m = [0] + list(map(int, input().split()))
C = [0] + list(map(int, input().split()))
dp = [[0 for __ in range(sum(C)+1)] for _ in range(N+1)]
result = 100*N+1

for i in range(N+1):
    for j in range(sum(C)+1):
        dp[i][j] = dp[i-1][j]

        if j < C[i]:
            continue

        dp[i][j] = max(dp[i-1][j-C[i]]+m[i], dp[i][j])

        if dp[i][j] >= M:
            result = min(result, j)

print(result)
