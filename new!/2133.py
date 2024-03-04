N = int(input())

dp = [0 for _ in range(31)]
dp[2] = 3
dp[4] = 11

for i in range(6, 31, 2):
    if i % 2 == 1:
        continue

    dp[i] = dp[i-2]*3+sum(dp[:i-2])*2+2
print(dp[N])
