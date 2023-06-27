from itertools import combinations
def bfs(x,y):
    global N,M
    count=1
    for i in range(4):
        nx=x+n_x[i]
        ny=y+n_y[i]
        if 0<=nx<=N-1 and 0<=ny<=M-1 and new_lab[nx][ny]==0:
            new_lab[nx][ny]=2
            count+=bfs(nx,ny)
    return count

N,M=list(map(int,input().split()))
lab=[list(map(int,input().split())) for _ in range(N)]
empty,virus=[],[]
n_x=[0,0,1,-1]
n_y=[-1,1,0,0]
result=0
for i in range(N):
    for j in range(M):
        if lab[i][j]==0:
            empty.append([i,j])
        if lab[i][j]==2:
            virus.append([i,j])

block_count=N*M-len(empty)-len(virus)+3
for block in combinations(empty,3):
    [x1,y1],[x2,y2],[x3,y3]=block
    new_lab=[_[:] for _ in lab]
    new_lab[x1][y1]=1
    new_lab[x2][y2]=1
    new_lab[x3][y3]=1
    
    count=0
    for vx,vy in virus:
        count+=bfs(vx,vy)
    result=max(result,N*M-block_count-count)
print(result)
