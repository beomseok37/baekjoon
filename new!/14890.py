import sys
input = sys.stdin.readline

N, L = list(map(int, input().split()))
board = [list(map(int, input().split())) for _ in range(N)]
answer = 0


def doRow(i, j):
    global answer
    current = board[i][j]
    t = j+1
    length = 1
    while t < N:
        if abs(board[i][t]-current) > 1:
            return
        elif board[i][t] == current:
            length += 1
            t += 1
        elif board[i][t] > current:
            if length < L:
                return

            current = board[i][t]
            length = 1
            t += 1
        else:
            current = board[i][t]
            lowLength = 0
            while t < N and board[i][t] == current:
                lowLength += 1
                t += 1

            if lowLength < L:
                return

            if t == N:
                break

            length = lowLength-L

    answer += 1


def doColumn(i, j):
    global answer
    current = board[j][i]
    t = j+1
    length = 1
    while t < N:
        if abs(board[t][i]-current) > 1:
            return
        elif board[t][i] == current:
            length += 1
            t += 1
        elif board[t][i] > current:
            if length < L:
                return

            current = board[t][i]
            length = 1
            t += 1
        else:
            current = board[t][i]
            lowLength = 0
            while t < N and board[t][i] == current:
                lowLength += 1
                t += 1

            if lowLength < L:
                return

            if t == N:
                break

            length = lowLength-L

    answer += 1


for i in range(N):
    doRow(i, 0)
    doColumn(i, 0)
print(answer)
