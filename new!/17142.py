from itertools import combinations
from collections import deque

N, M = list(map(int, input().split()))
board = [list(map(int, input().split())) for _ in range(N)]
moves = [(-1, 0), (0, -1), (0, 1), (1, 0)]
viruses = []
answer = 2501
notWallCount = N*N

for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            viruses.append((i, j))
        if board[i][j] == 1:
            notWallCount -= 1


for virusPositions in combinations(viruses, M):
    visited = [[-1 for _ in range(N)] for __ in range(N)]
    queue = deque()
    for vPos in virusPositions:
        visited[vPos[0]][vPos[1]] = 0
        queue.append((vPos[0], vPos[1], 0))
    while queue:
        r, c, count = queue.popleft()

        for i in range(4):
            nr, nc = r+moves[i][0], c+moves[i][1]

            if not (0 <= nr < N and 0 <= nc < N) or board[nr][nc] == 1 or visited[nr][nc] != -1:
                continue

            visited[nr][nc] = count+1
            queue.append((nr, nc, count+1))

    temp = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                if visited[i][j] == -1:
                    temp = 2501
                else:
                    temp = max(temp, visited[i][j])

    answer = min(answer, temp)
print(answer if answer != 2501 else -1)
