from collections import deque

N, M, fuels = list(map(int, input().split()))
board = [list(map(int, input().split())) for _ in range(N)]
taxiR, taxiC = list(map(int, input().split()))
passengerBoard = [[-1 for _ in range(N)] for __ in range(N)]
arrivalPoses = []
for i in range(M):
    sr, sc, er, ec = list(map(int, input().split()))
    passengerBoard[sr-1][sc-1] = i
    arrivalPoses.append([er-1, ec-1])
arrivalCheck = [False for _ in range(M)]
moves = [(-1, 0), (0, -1), (0, 1), (1, 0)]


def findPassengers(sr, sc):
    visited = [[False for _ in range(N)] for __ in range(N)]
    visited[sr][sc] = True
    queue = deque([(sr, sc, 0)])
    passengerList = []
    shortestDistance = -1
    while queue:
        r, c, distance = queue.popleft()

        if shortestDistance != -1 and distance > shortestDistance:
            break

        passenger = passengerBoard[r][c]
        if passenger != -1 and not arrivalCheck[passenger]:
            shortestDistance = distance
            passengerList.append([passenger, r, c])

        for i in range(4):
            nr, nc = moves[i][0]+r, moves[i][1]+c

            if not (0 <= nr < N and 0 <= nc < N) or visited[nr][nc] or board[nr][nc] == 1:
                continue

            visited[nr][nc] = True
            queue.append((nr, nc, distance+1))

    if not passengerList:
        return [-1, -1, -1, -1]
    passenger, pr, pc = passengerList[0]
    for i in range(1, len(passengerList)):
        nPassenger, npr, npc = passengerList[i]
        if npr < pr or (npr == pr and npc < pc):
            passenger, pr, pc = nPassenger, npr, npc

    return [passenger, shortestDistance, pr, pc]


def findArrival(sr, sc, er, ec):
    visited = [[False for _ in range(N)] for __ in range(N)]
    visited[sr][sc] = True
    queue = deque([(sr, sc, 0)])
    while queue:
        r, c, distance = queue.popleft()

        if r == er and c == ec:
            return distance

        for i in range(4):
            nr, nc = moves[i][0]+r, moves[i][1]+c

            if not (0 <= nr < N and 0 <= nc < N) or visited[nr][nc] or board[nr][nc] == 1:
                continue

            visited[nr][nc] = True
            queue.append((nr, nc, distance+1))
    return -1


moveCount = 0
sr, se = taxiR-1, taxiC-1
while moveCount < M:
    passenger, distance, pr, pc = findPassengers(sr, se)
    fuels -= distance
    if passenger == -1 or fuels < 0:
        fuels = -1
        break

    distance = findArrival(
        pr, pc, arrivalPoses[passenger][0], arrivalPoses[passenger][1])
    fuels -= distance
    if distance == -1 or fuels < 0:
        fuels = -1
        break

    fuels += distance*2
    arrivalCheck[passenger] = True
    sr, se = arrivalPoses[passenger][0], arrivalPoses[passenger][1]
    moveCount += 1

print(fuels)
