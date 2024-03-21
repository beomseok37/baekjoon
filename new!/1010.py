import sys
input = sys.stdin.readline


def find(n, m):
    if n > m:
        return 0

    if dp[n][m] != 0:
        return dp[n][m]

    dp[n][m] = find(n-1, m-1)+find(n, m-1)
    return dp[n][m]


T = int(input())
dp = [[0 for _ in range(31)] for __ in range(31)]
for i in range(31):
    dp[1][i] = i

for _ in range(T):
    N, M = list(map(int, input().split()))

    print(find(N, M))
