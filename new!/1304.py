import sys
input = sys.stdin.readline

def find(node):
    if node == parent[node]:
        return node
    parent[node] = find(parent[node])
    return parent[node]

def union(node1,node2):
    node1_parent = find(node1)
    node2_parent = find(node2)
    if node1_parent != node2_parent:
        parent[node2_parent] = node1_parent

N,M = list(map(int,input().split()))
parent = [i for i in range(N+1)]

for _ in range(M):
    S,E = list(map(int,input().split()))
    if S > E:
        for node in range(E,S):
            union(S,node)
    
result=1
for i in range(1,N):
    if N%i==0:
        for j in range(1,N//i):
            parent1 = find(j*i)
            parent2 = find(j*i+1)
            if parent1 == parent2:
                break
        else:
            result = N//i
            break
print(result)
