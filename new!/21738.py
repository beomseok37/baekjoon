import sys
input = sys.stdin.readline

N,S,P = list(map(int,input().split()))
link = {}
info = []

for _ in range(N-1):
    A,B = list(map(int,input().split()))
    if A not in link:
        link[A] = []
    if B not in link:
        link[B] = []
    link[A].append(B)
    link[B].append(A)
        
visited = [False for _ in range(N+1)]
visited[P] = True
stack = [[P,0]]
depth = 0
while stack:
    node,new_depth = stack.pop()
    
    if node <= S:
        info.append(new_depth)
    
    for new_node in link[node]:
        if not visited[new_node]:
            visited[new_node]=True
            stack.append([new_node,new_depth+1])
    
    
info.sort()
print(N-1-info[0]-info[1])
