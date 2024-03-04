N = int(input())
A = list(map(int, input().split()))
dp = [[[] for _ in range(N)] for __ in range(N)]
answer = [A[0]]

dp[0][0].append(A[0])
for i in range(1, N):
    if A[0] < A[i]:
        dp[0][i].append(A[0])
    dp[0][i].append(A[i])

    if len(dp[0][i]) > len(answer):
        answer = dp[0][i][:]

for i in range(1, N):
    dp[i][i].extend(dp[i-1][i])
    for j in range(i+1, N):
        if A[j] > A[i]:
            if len(dp[i][i])+1 > len(dp[i-1][j]):
                dp[i][j].extend(dp[i][i])
                dp[i][j].append(A[j])
            else:
                dp[i][j].extend(dp[i-1][j])
        else:
            dp[i][j].extend(dp[i-1][j])
        if len(dp[i][j]) > len(answer):
            answer = dp[i][j][:]
print(len(answer))
print(' '.join(map(str, answer)))
