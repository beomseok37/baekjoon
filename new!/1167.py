import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

def dfs(node, distance):
    for nowNode, nowDistance in graph[node]:
        if dp[nowNode] == -1:
            dp[nowNode] = nowDistance + distance 
            dfs(nowNode, nowDistance + distance)

V = int(input())
graph = [[] for _ in range(V+1)]
for i in range(V):
    temp = list(map(int,input().split()))
    for j in range(1,len(temp)-2,2):
        graph[temp[0]].append([temp[j],temp[j+1]])

dp = [-1 for _ in range(V+1)]
dp[1]=0
dfs(1,0)
longestNode=dp.index(max(dp))

dp = [-1 for _ in range(V+1)]
dp[longestNode]=0
dfs(longestNode,0)
print(max(dp))
