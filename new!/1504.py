import sys
from collections import deque
input = sys.stdin.readline


def find(start, end):
    visited = [sys.maxsize for _ in range(N+1)]
    queue = deque([(start, 0)])
    visited[start] = 0
    while queue:
        node, length = queue.popleft()

        for newNode, newLength in edges[node]:
            if visited[newNode] < length+newLength:
                continue

            visited[newNode] = length+newLength
            queue.append((newNode, length+newLength))
    return visited[end]


N, E = list(map(int, input().split()))
edges = [[] for _ in range(N+1)]
for _ in range(E):
    a, b, c = list(map(int, input().split()))
    edges[a].append((b, c))
    edges[b].append((a, c))
nodes = list(map(int, input().split()))
result1 = [0, 0, 0]
result2 = [0, 0, 0]

result1[0] = find(1, nodes[0])
result2[0] = find(1, nodes[1])
result1[1] = find(nodes[0], nodes[1])
result2[1] = result1[1]
result1[2] = find(nodes[1], N)
result2[2] = find(nodes[0], N)
answer = min(sum(result1), sum(result2))
print(answer if answer < sys.maxsize else -1)
