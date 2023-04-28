from collections import deque
import sys
input = sys.stdin.readline

T=int(input())
for _ in range(T):
    V,E=list(map(int,input().split()))
    edges={}
    
    for i in range(1,V+1):
        edges[i]=[]
        
    for i in range(E):
        a,b=list(map(int,input().split()))
        edges[a].append(b)
        edges[b].append(a)
    
    node_color=[0 for __ in range(V+1)]
    for i in range(1,V+1):
        if node_color[i]!=0:
            continue
        
        queue=deque()
        queue.append(i)
        node_color[i]=1
        answer='YES'
        while queue:
            node =queue.popleft()
            
            for next_node in edges[node]:
                if node_color[next_node]==0:
                    node_color[next_node]=node_color[node]*(-1)
                    queue.append(next_node)
                elif node_color[next_node]==node_color[node]:
                    answer='NO'
                    break
                
            if answer=='NO':
                break
        if answer=='NO':
            break
    print(answer)
