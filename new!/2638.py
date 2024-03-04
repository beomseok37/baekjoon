import sys
sys.setrecursionlimit(10**6)
N, M = list(map(int, input().split()))
board = [[0 for _ in range(M+2)]]
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
cheese = 0
for _ in range(N):
    temp = [0]
    temp.extend(list(map(int, input().split())))
    temp.append(0)
    board.append(temp)
board.append([0 for _ in range(M+2)])

for i in range(1, N+1):
    cheese += sum(board[i])


def checkOutside(i, j):
    for k in range(4):
        ni, nj = i+moves[k][0], j+moves[k][1]

        if not (0 <= ni < N+2 and 0 <= nj < M+2) or board[ni][nj] == 1 or isOutside[ni][nj] == True:
            continue

        isOutside[ni][nj] = True
        checkOutside(ni, nj)


def checkCheese(i, j):
    count = 0
    for k in range(4):
        ni, nj = i+moves[k][0], j+moves[k][1]

        if not (1 <= ni <= N and 1 <= nj <= M) or board[ni][nj] == 1:
            continue

        if isOutside[ni][nj]:
            count += 1

    return count > 1


count = 0
while cheese > 0:
    isOutside = [[False for _ in range(M+2)] for _ in range(N+2)]
    isOutside[0][0] = True
    checkOutside(0, 0)

    meltedCheese = []
    for i in range(1, N+1):
        for j in range(1, M+1):
            if board[i][j] == 1 and checkCheese(i, j):
                meltedCheese.append((i, j))

    for i, j in meltedCheese:
        board[i][j] = 0

    cheese -= len(meltedCheese)
    count += 1

print(count)
