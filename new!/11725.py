N=int(input())
edges={}
parent=[0 for _ in range(N+1)]
visited=[False for _ in range(N+1)]
for i in range(N-1):
    a,b=list(map(int,input().split()))
    if a not in edges:
        edges[a]=[]
    if b not in edges:
        edges[b]=[]
    edges[a].append(b)
    edges[b].append(a)

stack=[1]
visited[1]=True
while stack:
    node =stack.pop(0)
    
    for next_node in edges[node]:
        if not visited[next_node]:
            parent[next_node]=node
            visited[next_node]=True
            stack.append(next_node)
            
for i in range(2,N+1):
    print(parent[i])
