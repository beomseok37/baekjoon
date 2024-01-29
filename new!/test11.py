from collections import deque
import sys
input = sys.stdin.readline

R, C = map(int, input().rstrip().split(' '))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
answer = 'FAIL'

visited = [[False for _ in range(C)] for _ in range(R)]
graph = []

for _ in range(R):
    graph.append(list(input().rstrip()))

start_x, start_y = 0, 0
rains = []

for y in range(R):
    for x in range(C):
        if graph[y][x] == 'W':
            start_x = x
            start_y = y
        if graph[y][x] == '*':
            rains.append((y, x))


def rain():
    global rains
    new_rains = []
    for y, x in rains:
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or ny >= R or nx < 0 or nx >= C:
                continue

            if graph[ny][nx] == '.':
                graph[ny][nx] == '*'
                new_rains.append((ny, nx))

    rains = list(set(rains+new_rains))


def bfs(start_y, start_x):
    q = deque()
    ex_cnt = 0
    visited[start_y][start_x] = True
    q.append((start_y, start_x, 0))
    rain()

    while q:
        cy, cx, cnt = q.popleft()

        if ex_cnt != cnt:
            rain()

        ex_cnt = cnt

        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]

            if ny < 0 or ny >= R or nx < 0 or nx >= C:
                continue

            if graph[ny][nx] == 'H':
                return cnt + 1

            if graph[ny][nx] == '.':
                if visited[ny][nx] == False:
                    visited[ny][nx] = True
                    q.append((ny, nx, cnt+1))

    return 'FAIL'


answer = bfs(start_y, start_x)
print(answer)
