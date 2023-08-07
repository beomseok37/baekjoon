import sys
from collections import defaultdict
input = sys.stdin.readline
sys.setrecursionlimit(10**5+1)

def recursion(node):
    for newNode in edges[node]:
        if not visited[newNode]:
            visited[newNode]=True
            toParent[newNode]=node
            recursion(newNode)

def visitParent(node):
    visited[node]=True
    if node==1:
        return
    visitParent(toParent[node])
    
def findCommonParent(node):
    global answer
    
    if visited[node]:
        answer=node
        return
    
    findCommonParent(toParent[node])

N=int(input())
edges=defaultdict(list)
for _ in range(N-1):
    a,b=list(map(int,input().split()))
    edges[a].append(b)
    edges[b].append(a)
M=int(input())
mList = [list(map(int,input().split())) for _ in range(M)]
visited=[False for _ in range(N+1)]
visited[1]=True
toParent={}
recursion(1)

for a,b in mList:
    answer=1
    visited=[False for _ in range(N+1)]
    visitParent(a)
    findCommonParent(b)
    print(answer)
