import sys
input = sys.stdin.readline

def find(x):
    if parent[x] == x:
        return x
    parent[x]=find(parent[x])
    return parent[x]

def union(a,b):
    a=find(a)
    b=find(b)
    parent[a]=b

V,E=list(map(int,input().split()))
edge=[[] for _ in range(V+1)]
parent=[i for i in range(V+1)]
count=0
for i in range(E):
    a,b=list(map(int,input().split()))
    if find(a)!=find(b):
        a,b=max(a,b),min(a,b)
        union(a,b)
    edge[a].append([b,i])
    edge[b].append([a,i])

p=find(1)
for node in range(2,V+1):
    if p!=find(node):
        print('NO')
        exit()

for each in edge:
    if len(each)%2==1:
        count+=1
print('YES' if count==2 or count==0 else 'NO')
