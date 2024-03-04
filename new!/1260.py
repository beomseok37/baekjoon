from collections import deque

N, M, V = list(map(int, input().split()))
edges = [set() for _ in range(N+1)]
for _ in range(M):
    temp = list(map(int, input().split()))
    edges[temp[0]].add(temp[1])
    edges[temp[1]].add(temp[0])

bfs = []
dfs = [V]

for i in range(1, N+1):
    edges[i] = list(edges[i])
    edges[i].sort()

visited = [False for _ in range(N+1)]
visited[V] = True
stack = [V]
while stack:
    node = stack.pop()
    if not visited[node]:
        dfs.append(node)
    visited[node] = True

    for i in range(len(edges[node])-1, -1, -1):
        if visited[edges[node][i]]:
            continue

        stack.append(edges[node][i])

visited = [False for _ in range(N+1)]
visited[V] = True
queue = deque([V])
while queue:
    node = queue.popleft()
    bfs.append(node)

    for nextNode in edges[node]:
        if visited[nextNode]:
            continue

        visited[nextNode] = True
        queue.append(nextNode)

print(' '.join(map(str, dfs)))
print(' '.join(map(str, bfs)))
