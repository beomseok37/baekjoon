def melt(i,j):
    global N,M
    count=0
    for k in range(4):
        ni,nj=i+di[k],j+dj[k]
        
        if 0<=ni<N and 0<=nj<M and bing[ni][nj]==0:
            count+=1
    
    bing[ni][nj]=max(bing[ni][nj]-count,0)


N,M = list(map(int,input().split()))
bing=[list(map(int,input().split())) for _ in range(N)]
di,dj=[-1,1,0,0],[0,0,-1,1]
count=0
for i in range(N):
    for j in range(M):
        if bing[i][j]!=0:
            count+=1

year=0
while count!=0:
    year+=1
    flag=False
    for i in range(N):
        for j in range(M):
            if bing[i][j]==0:
                continue
            
            flag=True
            newBing=[bing[k][:] for k in range(N)]
            visited=[[False for _ in range(M)] for __ in range(N)]
            stack=[[i,j]]
            visited[i][j]=True
            while stack:
                ni,nj=stack.pop()
                
                count2=0
                for k in range(4):
                    nni,nnj=ni+di[k],nj+dj[k]
                    
                    if 0<=nni<N and 0<=nnj<M:
                        if bing[nni][nnj]==0:
                            count2+=1
                        elif not visited[nni][nnj]:
                            visited[nni][nnj]=True
                            stack.append([nni,nnj])
                
                newBing[ni][nj]=max(bing[ni][nj]-count2,0)
                
                if newBing[ni][nj]==0:
                    count-=1
            
            bing=[newBing[k][:] for k in range(N)]
            
            if flag:
                break
        if flag:
            break
    
    flag=False
    for i in range(N):
        for j in range(M):
            if bing[i][j]==0:
                continue
            
            flag=True
            visited=[[False for _ in range(M)] for __ in range(N)]
            stack=[[i,j]]
            visited[i][j]=True
            temp=0
            while stack:
                ni,nj=stack.pop()
                temp+=1
                for k in range(4):
                    nni,nnj=ni+di[k],nj+dj[k]
                    
                    if 0<=nni<N and 0<=nnj<M and bing[nni][nnj]!=0 and not visited[nni][nnj]:
                        visited[nni][nnj]=True
                        stack.append([nni,nnj])
            
            if count!=temp:
                print(year)
                exit()
            
            if flag:
                break
        if flag:
            break
print(0)
