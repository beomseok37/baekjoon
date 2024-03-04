def findEachIsland(i, j, num):
    global N, M
    for k in range(4):
        ni, nj = i+moves[k][0], j+moves[k][1]
        if not (0 <= ni < N and 0 <= nj < M) or visited[ni][nj] or board[ni][nj] == 0:
            continue

        visited[ni][nj] = num
        islands[num].append((ni, nj))
        findEachIsland(ni, nj, num)


def findEachEdges(i, j, nextMoves, num, count):
    if visited[i][j] == 0:
        ni, nj = i+nextMoves[0], j+nextMoves[1]
        if not (0 <= ni < N and 0 <= nj < M):
            return

        findEachEdges(ni, nj, nextMoves, num, count+1)
    else:
        if visited[i][j] != num and count >= 2:
            newIsland = visited[i][j]
            if edges[newIsland][num] == 0:
                newCount = count if edges[num][newIsland] == 0 else min(
                    edges[num][newIsland], count)
                edges[num][newIsland] = newCount
                allEdges.append((newCount, num, newIsland))
            else:
                edges[num][newIsland] = edges[newIsland][num]
        else:
            return


def find(node):
    if parent[node] == node:
        return node
    parent[node] = find(parent[node])
    return parent[node]


def union(a, b):
    pa = find(a)
    pb = find(b)

    if pa != pb:
        parent[pa] = pb
    return pa != pb


N, M = list(map(int, input().split()))
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for __ in range(N)]
islands = [[] for _ in range(7)]
edges = [[0 for __ in range(7)] for _ in range(7)]
allEdges = []
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
parent = [i for i in range(7)]
answer = 0

num = 1
for i in range(N):
    for j in range(M):
        if board[i][j] == 1 and not visited[i][j]:
            visited[i][j] = num
            islands[num].append((i, j))
            findEachIsland(i, j, num)
            num += 1

for i in range(1, num):
    for x, y in islands[i]:
        for j in range(4):
            nx, ny = x+moves[j][0], y+moves[j][1]

            if not (0 <= nx < N and 0 <= ny < M) or visited[nx][ny] == i:
                continue

            findEachEdges(nx, ny, moves[j], i, 0)

allEdges.sort()
for count, n1, n2 in allEdges:
    answer += count if union(n1, n2) else 0

for i in range(1, num-1):
    if find(i) != find(i+1):
        answer = -1
        break
print(answer)
