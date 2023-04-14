import heapq

def find(a):
    if parent[a]==a:
        return a
    
    parent[a]=find(parent[a])
    return parent[a]

def union(a,b):
    parent_a=find(a)
    parent_b=find(b)
    
    if parent_a==parent_b:
        return False
    
    parent[parent_a]=parent_b
    return True

N,C=list(map(int,input().split()))
positions=[list(map(int,input().split())) for _ in range(N)]
edges=[]
parent=[i for i in range(N)]

for i in range(N-1):
    for j in range(i+1,N):
        cost=(positions[i][0]-positions[j][0])**2 + (positions[i][1]-positions[j][1])**2
        
        if cost>=C:
            heapq.heappush(edges,[cost,i,j])

edge_count=0
total_cost=0
while edges:
    cost,i,j = heapq.heappop(edges)
    
    if union(i,j):
        edge_count+=1
        total_cost+=cost
    
    if edge_count==N-1:
        break

print(total_cost if edge_count==N-1 else -1)
