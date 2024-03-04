N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0, 0, 0] for _ in range(N)] for __ in range(N)]

dp[0][1][0] = 1

for r in range(0, N):
    for c in range(1, N):
        if c+1 < N and board[r][c+1] == 0:
            dp[r][c+1][0] = dp[r][c][0]+dp[r][c][2]

        if r+1 < N and board[r+1][c] == 0:
            dp[r+1][c][1] = dp[r][c][1]+dp[r][c][2]

        if r+1 < N and c+1 < N and board[r+1][c] == 0 and board[r][c+1] == 0 and board[r+1][c+1] == 0:
            dp[r+1][c+1][2] = sum(dp[r][c])

print(sum(dp[N-1][N-1]))
