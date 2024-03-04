N = int(input())
board = []
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
maxHeight = 0
minHeight = 101

for i in range(N):
    temp = list(map(int, input().split()))
    minHeight = min(minHeight, min(temp))
    maxHeight = max(maxHeight, max(temp))
    board.append(temp)


answer = 1
for h in range(minHeight, maxHeight+1):
    visited = [[False for _ in range(N)] for __ in range(N)]
    temp = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] or board[i][j] <= h:
                continue

            temp += 1
            stack = [(i, j)]
            while stack:
                ci, cj = stack.pop()

                for k in range(4):
                    ni, nj = ci+moves[k][0], cj+moves[k][1]

                    if not (0 <= ni < N and 0 <= nj < N) or visited[ni][nj] or board[ni][nj] <= h:
                        continue

                    visited[ni][nj] = True
                    stack.append((ni, nj))

    answer = max(answer, temp)
print(answer)
