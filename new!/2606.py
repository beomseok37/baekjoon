N = int(input())
M = int(input())
edges = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = list(map(int, input().split()))
    edges[a].append(b)
    edges[b].append(a)

stack = [1]
visited = [False for _ in range(N+1)]
visited[1] = True
answer = 0
while stack:
    node = stack.pop()

    for newNode in edges[node]:
        if visited[newNode]:
            continue

        answer += 1
        visited[newNode] = True
        stack.append(newNode)
print(answer)
