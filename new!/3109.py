import sys
input = sys.stdin.readline


def dfs(x, y):
    global R, C
    if y == C-1:
        return True

    flag = False
    for i in range(3):
        nx, ny = moves[i][0]+x, moves[i][1]+y

        if not (0 <= nx < R and 0 <= ny < C) or visited[nx][ny] or roads[nx][ny] == 'x':
            continue

        visited[nx][ny] = True
        if dfs(nx, ny):
            flag = True
            break

    return flag


R, C = list(map(int, input().split()))
roads = [list(input()) for _ in range(R)]
visited = [[False for _ in range(C)] for __ in range(R)]
moves = [(-1, 1), (0, 1), (1, 1)]
answer = 0

for r in range(R):
    visited[r][0] = True
    if dfs(r, 0):
        answer += 1

print(answer)
