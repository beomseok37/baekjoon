R, C, K = list(map(int, input().split()))
board = []
hots = []
checks = []
temperature = [[0 for _ in range(C)] for __ in range(R)]
for i in range(R):
    temp = list(map(int, input().split()))
    for j in range(C):
        if temp[j] == 0:
            continue
        if temp[j] == 5:
            checks.append((i, j))
        else:
            hots.append([temp[j], i, j])
    board.append(temp)

W = int(input())

for _ in range(W):
    x, y, t = list(map(int, input().split()))
    if t == 0:
        if x > 1:
            board[x-1][y-1] += 40
            board[x-2][y-1] += 80
    else:
        if y < C:
            board[x-1][y-1] += 10
            board[x-1][y] += 20


def hotRight(r, c, t):
    if t == 0 or c+1 >= C:
        return
    if r > 0 and (board[r][c]//10) & 4 == 0 and (board[r-1][c]//10) & 1 == 0 and not visited[r-1][c+1]:
        visited[r-1][c+1] = True
        temperature[r-1][c+1] += t
        hotRight(r-1, c+1, t-1)

    if (board[r][c]//10) & 1 == 0 and not visited[r][c+1]:
        visited[r][c+1] = True
        temperature[r][c+1] += t
        hotRight(r, c+1, t-1)

    if r < R-1 and (board[r][c]//10) & 8 == 0 and (board[r+1][c]//10) & 1 == 0 and not visited[r+1][c+1]:
        visited[r+1][c+1] = True
        temperature[r+1][c+1] += t
        hotRight(r+1, c+1, t-1)


# 다음 위치 확인
# 현 위치 확인, 벽 확인, 방문 여부 확인

def hotLeft(r, c, t):
    if t == 0 or c < 1:
        return

    if r > 0 and (board[r][c]//10) & 4 == 0 and (board[r-1][c]//10) & 2 == 0 and not visited[r-1][c-1]:
        visited[r-1][c-1] = True
        temperature[r-1][c-1] += t
        hotLeft(r-1, c-1, t-1)

    if (board[r][c]//10) & 2 == 0 and not visited[r][c-1]:
        visited[r][c-1] = True
        temperature[r][c-1] += t
        hotLeft(r, c-1, t-1)

    if r < R-1 and (board[r][c]//10) & 8 == 0 and (board[r+1][c]//10) & 2 == 0 and not visited[r+1][c-1]:
        visited[r+1][c-1] = True
        temperature[r+1][c-1] += t
        hotLeft(r+1, c-1, t-1)


def hotUp(r, c, t):
    if t == 0 or r < 1:
        return

    if c > 0 and (board[r][c]//10) & 2 == 0 and (board[r][c-1]//10) & 4 == 0 and not visited[r-1][c-1]:
        visited[r-1][c-1] = True
        temperature[r-1][c-1] += t
        hotUp(r-1, c-1, t-1)

    if (board[r][c]//10) & 4 == 0 and not visited[r-1][c]:
        visited[r-1][c] = True
        temperature[r-1][c] += t
        hotUp(r-1, c, t-1)

    if c+1 < C and (board[r][c]//10) & 1 == 0 and (board[r][c+1]//10) & 4 == 0 and not visited[r-1][c+1]:
        visited[r-1][c+1] = True
        temperature[r-1][c+1] += t
        hotUp(r-1, c+1, t-1)


def hotDown(r, c, t):
    if t == 0 or r+1 >= R:
        return

    if c > 0 and (board[r][c]//10) & 2 == 0 and (board[r][c-1]//10) & 8 == 0 and not visited[r+1][c-1]:
        visited[r+1][c-1] = True
        temperature[r+1][c-1] += t
        hotDown(r+1, c-1, t-1)

    if (board[r][c]//10) & 8 == 0 and not visited[r+1][c]:
        visited[r+1][c] = True
        temperature[r+1][c] += t
        hotDown(r+1, c, t-1)

    if c+1 < C and (board[r][c]//10) & 1 == 0 and (board[r][c+1]//10) & 8 == 0 and not visited[r+1][c+1]:
        visited[r+1][c+1] = True
        temperature[r+1][c+1] += t
        hotDown(r+1, c+1, t-1)


def adjust(r, c):
    if c+1 < C and (board[r][c]//10) & 1 == 0:
        minusT = abs(temperature[r][c]-temperature[r][c+1])//4
        if temperature[r][c] > temperature[r][c+1]:
            minusTemperature[r][c] -= minusT
            minusTemperature[r][c+1] += minusT
        else:
            minusTemperature[r][c] += minusT
            minusTemperature[r][c+1] -= minusT
    if r+1 < R and (board[r][c]//10) & 8 == 0:
        minusT = abs(temperature[r][c]-temperature[r+1][c])//4
        if temperature[r][c] > temperature[r+1][c]:
            minusTemperature[r][c] -= minusT
            minusTemperature[r+1][c] += minusT
        else:
            minusTemperature[r][c] += minusT
            minusTemperature[r+1][c] -= minusT


def reduceTemperature():
    for i in range(1, R-1):
        temperature[i][0] = max(0, temperature[i][0]-1)
        temperature[i][C-1] = max(0, temperature[i][C-1]-1)
    for i in range(1, C-1):
        temperature[0][i] = max(0, temperature[0][i]-1)
        temperature[R-1][i] = max(0, temperature[R-1][i]-1)
    temperature[0][0] = max(0, temperature[0][0]-1)
    temperature[0][C-1] = max(0, temperature[0][C-1]-1)
    temperature[R-1][0] = max(0, temperature[R-1][0]-1)
    temperature[R-1][C-1] = max(0, temperature[R-1][C-1]-1)


apple = 0
while True:
    for kind, r, c in hots:
        visited = [[False for _ in range(C)] for __ in range(R)]
        if kind == 1 and (board[r][c]//10) & 1 == 0 and c+1 < C:
            temperature[r][c+1] += 5
            hotRight(r, c+1, 4)
        elif kind == 2 and (board[r][c]//10) & 2 == 0 and c > 0:
            temperature[r][c-1] += 5
            hotLeft(r, c-1, 4)
        elif kind == 3 and (board[r][c]//10) & 4 == 0 and r > 0:
            temperature[r-1][c] += 5
            hotUp(r-1, c, 4)
        elif kind == 4 and (board[r][c]//10) & 8 == 0 and r+1 < R:
            temperature[r+1][c] += 5
            hotDown(r+1, c, 4)

    minusTemperature = [[0 for _ in range(C)] for __ in range(R)]
    for i in range(R):
        for j in range(C):
            adjust(i, j)

    for i in range(R):
        for j in range(C):
            temperature[i][j] += minusTemperature[i][j]

    reduceTemperature()
    apple += 1

    if apple > 100:
        break

    for r, c in checks:
        if temperature[r][c] < K:
            break
    else:
        break

print(apple)
