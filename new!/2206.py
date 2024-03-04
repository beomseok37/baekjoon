from collections import deque
import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))
board = [list(map(int, list(input()[:-1]))) for _ in range(N)]
visited = [[[False, False] for _ in range(M)] for __ in range(N)]
moves = [(0, 1), (1, 0), (-1, 0), (0, -1)]

queue = deque([(0, 0, 0, 0)])
answer = -1
while queue:
    r, c, move, count = queue.popleft()

    if r == N-1 and c == M-1:
        answer = move+1
        break

    for i in range(4):
        nr, nc = r+moves[i][0], c+moves[i][1]

        if not (0 <= nr < N and 0 <= nc < M) or visited[nr][nc][count]:
            continue

        if board[nr][nc] == 1:
            if count == 0:
                visited[nr][nc][1] = True
                queue.append((nr, nc, move+1, 1))
        else:
            visited[nr][nc][count] = True
            queue.append((nr, nc, move+1, count))
print(answer)
