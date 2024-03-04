N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
maxPath = [[] for _ in range(N)]
visited = [False for _ in range(N)]


def findMaxPath(node):
    if len(maxPath[node]) != 0:
        return maxPath[node][:]

    returnMaxPath = [node]
    tempMaxPath = []
    for nextNode in range(N):
        if board[node][nextNode] == 0 or visited[nextNode]:
            continue

        visited[nextNode] = True
        temp = findMaxPath(nextNode)
        visited[nextNode] = False
        if len(temp) > len(tempMaxPath):
            tempMaxPath.clear()
            tempMaxPath.extend(temp[:])

    returnMaxPath.extend(tempMaxPath[:])
    maxPath[node].extend(returnMaxPath[:])
    return maxPath[node][:]


visited[0] = True
answer = findMaxPath(0)
print(len(answer))
print(' '.join(map(lambda x: str(x+1), answer)))
