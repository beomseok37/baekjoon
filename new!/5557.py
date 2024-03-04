N = int(input())
A = list(map(int, input().split()))
dp = [0 for _ in range(21)]

dp[A[0]] = 1
for i in range(1, N-1):
    temp = [0 for _ in range(21)]

    for j in range(21):
        if j-A[i] >= 0:
            temp[j-A[i]] += dp[j]
        if j+A[i] <= 20:
            temp[j+A[i]] += dp[j]
    dp = temp[:]

print(dp[A[N-1]])
