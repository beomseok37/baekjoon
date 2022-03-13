def poly(count,total,x,y):
    global answer
    if answer >= total+maxNumber*(4-count):
        return
    if count == 4:
        answer = max(answer,total)
        return
    nextX=[0,-1,1,0]
    nextY=[-1,0,0,1]

    for i in range(4):
        newX,newY = x+nextX[i],y+nextY[i]
        if 0<=newX<N and 0<=newY<M and not visited[newX][newY]:
            if count == 2:
                visited[newX][newY] = 1
                poly(count+1,total+paper[newX][newY],x,y)
                visited[newX][newY] = 0
            visited[newX][newY] = 1
            poly(count+1,total+paper[newX][newY],newX,newY)
            visited[newX][newY] = 0

N, M = list(map(int,input().split()))
paper = []
for i in range(N):
    paper.append(list(map(int,input().split())))
visited = [[0]*M for i in range(N)]
answer = 0
maxNumber = max(map(max,paper))

for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        poly(1,paper[i][j],i,j)
        visited[i][j] = 0

print(answer)
