import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
def dfs(node):
    if dp[node]!=-1:
        return dp[node]
    total_max=0
    for next_node in edges[node]:
        prev_total=dfs(next_node)
        total_max=max(total_max,prev_total+D[next_node-1])
    
    dp[node]=total_max
    return dp[node]
        
T=int(input())
for t in range(T):
    N,K=list(map(int,input().split()))
    D=list(map(int,input().split()))
    edges=[[] for _ in range(N+1)]
    dp=[-1 for _ in range(N+1)]
    for _ in range(K):
        a,b=list(map(int,input().split()))
        edges[b].append(a)
    W=int(input())
    
    print(dfs(W)+D[W-1])
