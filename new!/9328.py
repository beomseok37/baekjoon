import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)

def dfs(x,y):
    global X,Y,answer
    
    if maps[x][y]=='$':
        answer+=1
        
    for i in range(4):
        nx,ny=moves[i][0]+x,moves[i][1]+y
        
        if not (0<=nx<X and 0<=ny<Y) or visited[nx][ny] or maps[nx][ny]=='*':
            continue
        
        now=maps[nx][ny]
        if 'A'<=now<='Z':
            if now.lower() in keys:
                maps[nx][ny]='.'
            else:
                door[now].append((nx,ny))
                continue
        
        if 'a'<=now<='z':
            keys.add(now)
        
        visited[nx][ny]=True
        dfs(nx,ny)
        
def find(x,y):
    global answer
    now=maps[x][y]
    
    if maps[x][y]=='*' or visited[x][y]:
        return 
    
    if 'A'<=now<='Z':
        if now.lower() in keys:
            maps[x][y]='.'
        else:
            door[now].append((x,y))
            return
    
    if 'a'<=now<='z':
        keys.add(now)

    visited[x][y]=True
    dfs(x,y)

T=int(input())
answerList=[]
for t in range(T):
    X,Y=list(map(int,input().split()))
    maps=[list(input()) for _ in range(X)]
    keys=set(list(input()))
    moves=[(-1,0),(1,0),(0,-1),(0,1)]
    door=defaultdict(list)
    visited=[[False for _ in range(Y)] for __ in range(X)]
    answer = 0

    for i in range(X):
        find(i,0)
        find(i,Y-1)
    for i in range(1,Y-1):
        find(0,i)
        find(X-1,i)

    while True:
        prevKeyLength=len(keys)
        
        for key in list(keys):
            for x,y in door[key.upper()]:
                if visited[x][y]:
                    continue
                
                maps[x][y]='.'
                visited[x][y]=True
                dfs(x,y)
        
        if prevKeyLength==len(keys):
            break

    answerList.append(answer)

for answer in answerList:
    print(answer)
