import sys
input = sys.stdin.readline

def recursion(node):
    visited=[False for _ in range(N+1)]
    stack=[[node,0]]

    while stack:
        now_node,now_count=stack.pop()
        
        if len(edges[now_node])==1:
            if leaf_nodes[now_node]>=now_count:
                leaf_nodes[now_node]=-1
            
        for new_node in edges[now_node]:
            if not visited[new_node]:
                visited[new_node]=True
                stack.append([new_node,now_count+1])
                
N=int(input())
edges={}
for i in range(N-1):
    temp1,temp2=list(map(int,input().split()))
    if temp1 not in edges:
        edges[temp1]=[]
    if temp2 not in edges:
        edges[temp2]=[]
    edges[temp1].append(temp2)
    edges[temp2].append(temp1)
    
a,b,c=list(map(int,input().split()))
visited=[False for _ in range(N+1)]
leaf_nodes=[0 for _ in range(N+1)]
nearest_nodes=[]

stack=[[a,0]]
visited[a]=True
while stack:
    now_node,now_count=stack.pop()
    
    if len(edges[now_node])==1:
        nearest_nodes.append(now_node)
        leaf_nodes[now_node]=now_count
            
    for new_node in edges[now_node]:
        if not visited[new_node]:
            visited[new_node]=True
            stack.append([new_node,now_count+1])

recursion(b)
recursion(c)

for nearest_node in nearest_nodes:
    if leaf_nodes[nearest_node]!=-1:
        print('YES')
        break
else:
    print('NO')
