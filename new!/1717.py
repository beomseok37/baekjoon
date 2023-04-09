import sys
input = sys.stdin.readline

n,m=list(map(int,input().split()))
operations=[list(map(int,input().split())) for _ in range(m)]
parent=[i for i in range(n+1)]
def find(node):
    if parent[node]==node:
        return node
    parent[node]=find(parent[node])
    return parent[node]

def union(a,b):
    parent_a=find(a)
    parent_b=find(b)
    if parent_a!=parent_b:
        parent[parent_a]=parent_b

for cal,a,b in operations:
    if cal==0:
        union(min(a,b),max(a,b))
    else:
        parent_a=find(a)
        parent_b=find(b)
        print('YES' if parent_a==parent_b else 'NO')
