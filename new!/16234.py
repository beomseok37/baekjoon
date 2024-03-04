from queue import deque
import sys
input = sys.stdin.readline

N, L, R = list(map(int, input().split()))
countries = [list(map(int, input().split())) for _ in range(N)]
moves = [(-1, 0), (1, 0), (0, 1), (0, -1)]
checks = deque([(i, j) for i in range(N) for j in range(N)])

day = 0
while True:
    flag = False
    unionList = []
    visited = [[False for _ in range(N)] for __ in range(N)]
    for _ in range(len(checks)):
        i, j = checks.popleft()
        if visited[i][j]:
            continue

        visited[i][j] = True
        total = countries[i][j]
        temp = [(i, j)]
        stack = [(i, j)]
        while stack:
            x, y = stack.pop()
            for k in range(4):
                nx, ny = x+moves[k][0], y+moves[k][1]

                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and L <= abs(countries[x][y]-countries[nx][ny]) <= R:
                    visited[nx][ny] = True
                    total += countries[nx][ny]
                    stack.append((nx, ny))
                    temp.append((nx, ny))

        if len(temp) != 1:
            flag = True
            average = total//len(temp)
            for i, j in temp:
                checks.append((i, j))
                countries[i][j] = average

    if not flag:
        break
    day += 1
print(day)
