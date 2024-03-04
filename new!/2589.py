from collections import deque

N, M = list(map(int, input().split()))
board = [list(input()) for _ in range(N)]
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
answer = 0

for i in range(N):
    for j in range(M):
        if board[i][j] == 'W':
            continue

        visited = [[-1 for _ in range(M)] for __ in range(N)]
        visited[i][j] = 0
        queue = deque([(i, j, 0)])
        temp = 0
        while queue:
            x, y, time = queue.popleft()
            temp = max(temp, time)

            for k in range(4):
                nx, ny = x+moves[k][0], y+moves[k][1]

                if not (0 <= nx < N and 0 <= ny < M) or board[nx][ny] == 'W' or visited[nx][ny] != -1:
                    continue

                visited[nx][ny] = time
                queue.append((nx, ny, time+1))

        answer = max(answer, temp)
print(answer)
