from collections import deque

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

temp = 1
visited = [[False for _ in range(N)] for __ in range(N)]
for i in range(N):
    for j in range(N):
        if visited[i][j] or board[i][j] == 0:
            continue

        stack = [(i, j)]
        visited[i][j] = True
        board[i][j] = -temp
        while stack:
            x, y = stack.pop()

            for dx, dy in moves:
                nx = x+dx
                ny = y+dy

                if not (0 <= nx < N and 0 <= ny < N) or visited[nx][ny] or board[nx][ny] == 0:
                    continue

                visited[nx][ny] = True
                board[nx][ny] = -temp
                stack.append((nx, ny))
        temp += 1

visited = [[False for _ in range(N)] for __ in range(N)]
answer = 10_001
for i in range(N):
    for j in range(N):
        if board[i][j] == 0:
            continue

        now = board[i][j]
        for dx, dy in moves:
            nx, ny = i+dx, j+dy

            if not (0 <= nx < N and 0 <= ny < N) or visited[nx][ny] or board[nx][ny] != 0:
                continue
            visited[nx][ny] = True

            visited2 = [[False for _ in range(N)] for __ in range(N)]
            visited2[nx][ny] = True
            queue = deque([(nx, ny, 0)])
            while queue:
                x, y, count = queue.popleft()

                if board[x][y] != 0 and board[x][y] != now:
                    answer = min(answer, count)
                    break

                for ddx, ddy in moves:
                    nnx, nny = x+ddx, y+ddy

                    if not (0 <= nnx < N and 0 <= nny < N) or visited2[nnx][nny]:
                        continue

                    queue.append((nnx, nny, count+1))
                    visited2[nnx][nny] = True
print(answer)
