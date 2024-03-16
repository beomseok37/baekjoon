import sys
from collections import deque
input = sys.stdin.readline

N, M = list(map(int, input().split()))
board = [list(input()) for _ in range(N)]
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
adjacentCount = [[0 for _ in range(M)] for __ in range(N)]
division = [[0 for _ in range(M)] for __ in range(N)]
answer = [[0 for _ in range(M)] for __ in range(N)]


def findMax(r, c, island):
    division[r][c] = island
    count = 1
    adjacentPos = [(r, c)]
    queue = deque([(r, c)])
    while queue:
        nowR, nowC = queue.popleft()
        for i in range(4):
            nr, nc = nowR+moves[i][0], nowC+moves[i][1]

            if not (0 <= nr < N and 0 <= nc < M) or division[nr][nc] != 0 or board[nr][nc] == '1':
                continue

            division[nr][nc] = island
            count += 1
            queue.append((nr, nc))
            adjacentPos.append((nr, nc))

    for ar, ac in adjacentPos:
        adjacentCount[ar][ac] = count

    maxCount = count
    for i in range(4):
        nr, nc = r+moves[i][0], c+moves[i][1]

        if not (0 <= nr < N and 0 <= nc < M) or division[nr][nc] != 0 or board[nr][nc] == '1':
            continue

        division[nr][nc] = island
        maxCount = max(maxCount, findMax(nr, nc, count+1, island))

    adjacentCount[r][c] = maxCount
    return adjacentCount[r][c]


def findAdjacentEmptyCount(r, c):
    count = 1
    adjacentIsland = set()
    for i in range(4):
        nr, nc = r+moves[i][0], c+moves[i][1]

        if not (0 <= nr < N and 0 <= nc < M):
            continue

        if division[nr][nc] in adjacentIsland:
            continue

        adjacentIsland.add(division[nr][nc])
        count += adjacentCount[nr][nc]
    return count


island = 1
for i in range(N):
    for j in range(M):
        if board[i][j] == '1' or division[i][j] != 0:
            continue
        division[i][j] = island
        findMax(i, j, island)
        island += 1

for i in range(N):
    for j in range(M):
        if board[i][j] == '0':
            continue
        answer[i][j] = findAdjacentEmptyCount(i, j) % 10

for i in range(N):
    print(''.join(map(str, answer[i])))
