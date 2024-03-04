from collections import defaultdict

N, M = list(map(int, input().split()))
edges = defaultdict(list)
for a, b, c in [list(map(int, input().split())) for _ in range(M)]:
    edges[a-1].append([b-1, c])
    edges[b-1].append([a-1, c])
start, end = list(map(lambda x: int(x)-1, input().split()))
visited = [False for _ in range(N)]
answer = 0


def dfs(currNode, currMinWeight):
    global answer
    if currNode == end:
        answer = max(answer, currMinWeight)
        return

    for nextNode, weight in edges[currNode]:
        if visited[nextNode]:
            continue

        visited[nextNode] = True
        dfs(nextNode, min(currMinWeight, weight))
        visited[nextNode] = False


visited[start] = True
dfs(start, 1_000_000_000)
print(answer)
