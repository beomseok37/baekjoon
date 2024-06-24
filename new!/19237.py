import sys
input = sys.stdin.readline

N, M, K = list(map(int, input().split()))
board = [list(map(int, input().split())) for _ in range(N)]
currentDirections = list(map(lambda x: int(x)-1, input().split()))
directionPriority = [[list(map(lambda x: int(x)-1, input().split()))
                      for __ in range(4)] for _ in range(M)]
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
smell = [[0 for _ in range(N)] for __ in range(N)]
whoseSmell = [[-1 for _ in range(N)] for __ in range(N)]
sharkPos = [[] for _ in range(M)]
alive = [True for _ in range(M)]

for i in range(N):
    for j in range(N):
        if board[i][j] != 0:
            sharkPos[board[i][j]-1].extend([i, j])

second = 0
count = M
while second <= 1000 and count > 1:
    second += 1
    # 모든 칸의 냄새 -1
    for i in range(N):
        for j in range(N):
            smell[i][j] = smell[i][j]-1 if smell[i][j] > 0 else 0
            if smell[i][j] == 0:
                whoseSmell[i][j] == -1

    # 지금 칸에 K남기기
    for i, (sharkI, sharkJ) in enumerate(sharkPos):
        if alive[i]:
            smell[sharkI][sharkJ] = K
            whoseSmell[sharkI][sharkJ] = i

    # 냄새 안나는 곳 방향 설정, 이미 같은 칸에 상어가 있다면 번호가 작은 상어가 살아남는다
    for i in range(M):
        if not alive[i]:
            continue

        sharkI, sharkJ = sharkPos[i]
        currentDirection = currentDirections[i]
        ni, nj = 0, 0

        for direction in directionPriority[i][currentDirection]:
            ni, nj = moves[direction][0]+sharkI, moves[direction][1]+sharkJ

            if not (0 <= ni < N and 0 <= nj < N) or smell[ni][nj] > 0:
                continue

            board[sharkI][sharkJ] = 0
            currentDirections[i] = direction
            if board[ni][nj] == 0:
                board[ni][nj] = i+1
                sharkPos[i] = [ni, nj]
            elif board[ni][nj] > i+1:
                board[ni][nj] = i+1
                sharkPos[i] = [ni, nj]
                alive[board[ni][nj]] = False
                count -= 1
            else:
                count -= 1
                alive[i] = False
            break
        else:
            for direction in directionPriority[i][currentDirection]:
                ni, nj = moves[direction][0]+sharkI, moves[direction][1]+sharkJ

                if not (0 <= ni < N and 0 <= nj < N) or whoseSmell[ni][nj] != i:
                    continue
                board[sharkI][sharkJ] = 0
                board[ni][nj] = i+1
                currentDirections[i] = direction
                sharkPos[i] = [ni, nj]
                break

print(second if second <= 1000 else -1)
