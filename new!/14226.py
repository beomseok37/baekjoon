from collections import deque
S = int(input())
dp = [[-1 for _ in range(S+1)] for _ in range(S+1)]

queue = deque([(1, 0)])
dp[1][0] = 0
while queue:
    num, copied = queue.popleft()

    if dp[num][num] == -1:
        dp[num][num] = dp[num][copied]+1
        queue.append((num, num))
    if num+copied <= S and dp[num+copied][copied] == -1:
        dp[num+copied][copied] = dp[num][copied]+1
        queue.append((num+copied, copied))
    if num >= 1 and dp[num-1][copied] == -1:
        dp[num-1][copied] = dp[num][copied]+1
        queue.append((num-1, copied))

answer = 5000
for i in range(S+1):
    if dp[S][i] != -1:
        answer = min(answer, dp[S][i])
print(answer)
