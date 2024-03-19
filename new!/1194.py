from collections import deque

N, M = list(map(int, input().split()))
board = [list(input()) for _ in range(N)]
visited = [[[False for _ in range(64)] for __ in range(M)] for ___ in range(N)]
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
ascii_A, ascii_F, ascii_a, ascii_f = ord('A'), ord('F'), ord('a'), ord('f')
queue = deque([])

for i in range(N):
    for j in range(M):
        if board[i][j] == '0':
            queue.append((i, j, 0, 0))
            visited[i][j][0] = True

while queue:
    r, c, count, keys = queue.popleft()

    if board[r][c] == '1':
        print(count)
        exit()

    for i in range(4):
        nr, nc = moves[i][0]+r, moves[i][1]+c

        if not (0 <= nr < N and 0 <= nc < M) or visited[nr][nc][keys] or board[nr][nc] == '#':
            continue

        num = ord(board[nr][nc])

        if ascii_A <= num <= ascii_F and (keys & (1 << (num-ascii_A)) == 0):
            continue

        newKeys = keys
        if ascii_a <= num <= ascii_f:
            newKeys |= (1 << (num-ascii_a))
        visited[nr][nc][newKeys] = True
        queue.append((nr, nc, count+1, newKeys))
print(-1)
