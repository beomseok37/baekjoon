N, K = list(map(int, input().split()))
W, V = [0], [0]
for _ in range(N):
    w, v = list(map(int, input().split()))
    W.append(w)
    V.append(v)

dp = [[0 for _ in range(K+1)] for __ in range(N+1)]
result = 0
for i in range(1, N+1):
    for j in range(K+1):
        dp[i][j] = dp[i-1][j]
        if W[i] > j:
            continue

        dp[i][j] = max(dp[i][j], dp[i-1][j-W[i]]+V[i])

print(dp[N][K])
