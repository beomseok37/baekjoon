import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
M = int(input())
questions = [list(map(lambda x: int(x)-1, input().split())) for _ in range(M)]
dp = [[0 for _ in range(N)] for __ in range(N)]

for j in range(N):
    for i in range(N):
        if i > j:
            continue

        if arr[i] == arr[j]:
            if i+1 == j or i == j:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i+1][j-1]

for s, e in questions:
    print(dp[s][e])
