from collections import defaultdict, deque
import sys
input = sys.stdin.readline

N, M, X = list(map(int, input().split()))
edges = defaultdict(list)
MAX_COUNT = 100_000_000
dp = [[MAX_COUNT for _ in range(N+1)] for __ in range(N+1)]
for _ in range(M):
    i, j, t = list(map(int, input().split()))

    edges[i].append((j, t))

for i in range(1, N+1):
    dp[i][i] = 0
    queue = deque([(i, 0)])

    while queue:
        node, count = queue.popleft()

        for nextNode, weight in edges[node]:
            if dp[i][nextNode] > count+weight:
                dp[i][nextNode] = count+weight
                queue.append((nextNode, count+weight))

answer = 0
for i in range(1, N+1):
    answer = max(answer, dp[i][X]+dp[X][i])
print(answer)
