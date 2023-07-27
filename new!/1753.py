import sys
from collections import defaultdict
from queue import PriorityQueue

input = sys.stdin.readline

V,E = list(map(int,input().split()))
K = int(input())
edges=defaultdict(list)
dp = [3000000 for _ in range(V+1)]

for i in range(E):
    u,v,w = list(map(int,input().split()))
    edges[u].append([v,w])

queue = PriorityQueue()
queue.put((0,K))
dp[K] = 0
while not queue.empty():
    weight,node = queue.get()
    
    if dp[node]<weight:
        continue
    
    for v,w in edges[node]:
        if weight+w<dp[v]:
            dp[v]=weight+w
            queue.put((weight+w,v))

for i in range(V):
    print(dp[i+1] if dp[i+1]!=3000000 else "INF")
