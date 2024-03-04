import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))
board = [list(map(int, input().split())) for _ in range(N)]
magics = [list(map(int, input().split())) for _ in range(M)]
marbleList = [0]
answer = [0, 0, 0]


def getList():
    move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = [[False for _ in range(N)] for __ in range(N)]
    visited[0][0] = True
    move_i = 0
    r, c = 0, 0
    while not (r == ((N+1)//2)-1 and c == ((N+1)//2)-1):
        while 0 <= r+move[move_i][0] < N and 0 <= c+move[move_i][1] < N and not visited[r+move[move_i][0]][c+move[move_i][1]]:
            r += move[move_i][0]
            c += move[move_i][1]
            visited[r][c] = True
            marbleList.append(board[r][c])
        move_i = (move_i+1) % 4


getList()
marbleList.reverse()
marbleList[0] = 4
# 위:1 아래:2 왼:3 오:4
for direction, length in magics:
    for i in range(1, length+1):
        temp = 4*i*i
        if direction == 1:
            temp += 3*i
        elif direction == 2:
            temp -= i
        elif direction == 3:
            temp -= 3*i
        else:
            temp += i
        if temp >= len(marbleList):
            break
        marbleList[temp] = -1

    flag = True
    while flag:
        flag = False
        start = 1
        while marbleList[start] == -1:
            start += 1

        now = marbleList[start]
        where = [start]
        for i in range(start+1, len(marbleList)):
            if marbleList[i] == -1 or marbleList[i] == 0:
                continue

            if marbleList[i] == now:
                where.append(i)
                continue

            if len(where) >= 4:
                flag = True
                for j in where:
                    answer[marbleList[j]-1] += 1
                    marbleList[j] = -1

            where = [i]
            now = marbleList[i]
        if len(where) >= 4:
            for j in where:
                answer[marbleList[j]-1] += 1
                marbleList[j] = -1

    temp = []
    for marble in marbleList:
        if marble != -1 and marble != 0:
            temp.append(marble)

    if len(temp) == 1:
        break

    marbleList = [4]
    now = temp[1]
    count = 1
    for i in range(2, len(temp)):
        if now == temp[i]:
            count += 1
            continue

        marbleList.append(count)
        marbleList.append(now)
        now = temp[i]
        count = 1

        if len(marbleList) == N*N:
            break
    if len(marbleList) != N*N:
        marbleList.append(count)
        marbleList.append(now)

print(answer[0]+2*answer[1]+3*answer[2])
