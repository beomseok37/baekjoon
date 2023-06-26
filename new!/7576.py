M,N=list(map(int,input().split()))
tomato=[list(map(int,input().split())) for _ in range(N)]

temp=[]
count=0
empty=0
for i in range(N):
    for j in range(M):
        if tomato[i][j]==1:
            temp.append([i,j])
            count+=1
        elif tomato[i][j]==-1:
            empty+=1
       
queue=[temp]
dx=[-1,1,0,0]
dy=[0,0,1,-1]
day=-1

while queue[0]:
    newTemp=[]
    for r,c in queue.pop():
        for i in range(4):
            nr,nc=r+dx[i],c+dy[i]
            
            if not (0<=nr<N and 0<=nc<M) or tomato[nr][nc]!=0:
                continue
            
            tomato[nr][nc]=1
            count+=1
            newTemp.append([nr,nc])
    queue.append(newTemp)
    day+=1
    
print(day if count==M*N-empty else -1)
