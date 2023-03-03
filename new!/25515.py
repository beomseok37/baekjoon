import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
def recursion(node):
    if len(edges[node])==0:
        return number[node]
    
    return_value=0
    for next_node in edges[node]:
        temp=recursion(next_node)
        if temp+number[node]>number[node]:
            return_value+=temp
            
    return return_value+number[node]

n = int(input())
edges=[[] for _ in range(n)]
for i in range(n-1):
    p,c=list(map(int,input().split()))
    edges[p].append(c)
number=list(map(int,input().split()))
print(recursion(0))
