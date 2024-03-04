import copy
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[0, 0] for _ in range(3)]

dp[0][0], dp[0][1] = board[0][0], board[0][0]
dp[1][0], dp[1][1] = board[0][1], board[0][1]
dp[2][0], dp[2][1] = board[0][2], board[0][2]
for i in range(1, N):
    temp = copy.deepcopy(dp)
    temp[0][0] = min(temp[0][0], temp[1][0])+board[i][0]
    temp[0][1] = max(temp[0][1], temp[1][1])+board[i][0]

    temp[1][0] = min(temp[0][0], temp[1][0], temp[2][0])+board[i][1]
    temp[1][1] = max(temp[0][1], temp[1][1], temp[2][1])+board[i][1]

    temp[2][0] = min(temp[1][0], temp[2][0])+board[i][2]
    temp[2][1] = max(temp[1][1], temp[2][1])+board[i][2]
    dp = temp

print(max(dp[0][1], dp[1][1], dp[2][1]),
      min(dp[0][0], dp[1][0], dp[2][0]))
