import sys
input = sys.stdin.readline

def bfs(s,t,count):
    global result
    if s==t:
        result=min(result,count)
        return
    
    bfs(s+1,t,count+1)
    if s*2<=t+3:
        bfs(s*2,t+3,count+1)

T=int(input())
for _ in range(T):
    S,T=list(map(int,input().split()))
    result=150
    bfs(S,T,0)
    print(result)
