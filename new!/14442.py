import sys
from collections import deque
input = sys.stdin.readline

N, M, K = list(map(int, input().split()))
board = [list(input()) for _ in range(N)]
visited = [[[0 for _ in range(K+1)] for __ in range(M)] for ___ in range(N)]
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

answer = -1
queue = deque([(0, 0, K)])
visited[0][0][K] = 1
while queue:
    r, c, breakCount = queue.popleft()

    if r == N-1 and c == M-1:
        answer = visited[r][c][breakCount]
        break

    for i in range(4):
        nr, nc = r+moves[i][0], c+moves[i][1]

        if not (0 <= nr < N and 0 <= nc < M):
            continue

        if board[nr][nc] == '1':
            if breakCount > 0 and visited[nr][nc][breakCount-1] == 0:
                visited[nr][nc][breakCount-1] = visited[r][c][breakCount]+1
                queue.append((nr, nc, breakCount-1))
        else:
            if visited[nr][nc][breakCount] == 0:
                visited[nr][nc][breakCount] = visited[r][c][breakCount]+1
                queue.append((nr, nc, breakCount))

print(answer)
