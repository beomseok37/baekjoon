import sys
input=sys.stdin.readline

N,Q=list(map(int,input().split()))
edges={}
for i in range(N-1):
    p,q,r=list(map(int,input().split()))
    if p not in edges:
        edges[p]=[]
    if q not in edges:
        edges[q]=[]
    edges[p].append([q,r])
    edges[q].append([p,r])

for i in range(Q):
    k,v=list(map(int,input().split()))
    visited=[False for _ in range(N+1)]
    queue=[[v,sys.maxsize]]
    count=0
    visited[v]=True
    while queue:
        node,usado = queue.pop(0)
        
        for next_node,next_usado in edges[node]:
            min_usado=min(usado,next_usado)
            if not visited[next_node] and min_usado>=k:
                visited[next_node]=True
                queue.append([next_node,min_usado])
                count+=1
    print(count)
