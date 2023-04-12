N,M=list(map(int,input().split()))
board=[list(input()) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if board[i][j]=='B':
            blue=[i,j]
        if board[i][j]=='R':
            red=[i,j]
stack=[[red[:],blue[:],0,'']]
while stack:
    [ri,rj],[bi,bj],count,s=stack.pop(0)
    
    if count==10:
        continue
    
    #위로 r,B와 벽까지의 거리를 구하고 먼저 도달한 애들에 따라서ㄲ
    flag=0
    nri,nrj,nbi,nbj=ri,rj,bi,bj
    if rj==bj:
        if ri>bi:
            while board[nbi-1][bj]!='#':
                nbi-=1
                if board[nbi][bj]=='O':
                    flag=1
            while board[nri-1][rj]!='#' and nri-1>nbi:
                nri-=1
                if flag!=1 and board[nri][rj]=='O':
                    flag=2
        else:
            while board[nri-1][rj]!='#':
                nri-=1
                if board[nri][rj]=='O':
                    flag=2
            if flag==2:
                nri-=1
            while board[nbi-1][bj]!='#' and nbi-1>nri:
                nbi-=1
                if board[nbi][bj]=='O':
                    flag=1
    else:
        while board[nri-1][rj]!='#':
            nri-=1
            if board[nri][rj]=='O':
                flag=2
        while board[nbi-1][bj]!='#':
            nbi-=1
            if board[nbi][bj]=='O':
                flag=1
    
    if flag==2 and count<10:
        print(count+1)
        break
    if flag==0 and (nri!=ri or nbi!=bi):
            stack.append([[nri,rj],[nbi,bj],count+1,s+'u'])    
    
    #오른쪽
    flag=0
    nri,nrj,nbi,nbj=ri,rj,bi,bj
    if ri==bi:
        if rj>bj:
            while board[ri][nrj+1]!='#':
                nrj+=1
                if board[ri][nrj]=='O':
                    flag=2
            if flag==2:
                nrj+=1
            while board[bi][nbj+1]!='#' and nbj+1<nrj:
                nbj+=1
                if board[bi][nbj]=='O':
                    flag=1
        else:
            while board[bi][nbj+1]!='#':
                nbj+=1
                if board[bi][nbj]=='O':
                    flag=1
            while board[ri][nrj+1]!='#' and nrj+1<nbj:
                nrj+=1
                if flag!=1 and board[ri][nrj]=='O':
                    flag=2
    else:
        while board[ri][nrj+1]!='#':
            nrj+=1
            if board[ri][nrj]=='O':
                flag=2
        while board[bi][nbj+1]!='#':
            nbj+=1
            if board[bi][nbj]=='O':
                flag=1
            
    if flag==2 and count<10:
        print(count+1)
        break
    if flag==0 and (nrj!=rj or nbj!=bj):
        stack.append([[ri,nrj],[bi,nbj],count+1,s+'r'])

    #아래로
    flag=0
    nri,nrj,nbi,nbj=ri,rj,bi,bj
    if rj==bj:
        if ri<bi:
            while board[nbi+1][bj]!='#':
                nbi+=1
                if board[nbi][bj]=='O':
                    flag=1
            while board[nri+1][rj]!='#' and nri+1<nbi:
                nri+=1
                if flag!=1 and board[nri][rj]=='O':
                    flag=2
        else:
            while board[nri+1][rj]!='#':
                nri+=1
                if board[nri][rj]=='O':
                    flag=2
            if flag==2:
                nri+=1
            while board[nbi+1][bj]!='#' and nbi+1<nri:
                nbi+=1
                if board[nbi][bj]=='O':
                    flag=1
    else:
        while board[nri+1][rj]!='#':
            nri+=1
            if board[nri][rj]=='O':
                flag=2
        while board[nbi+1][bj]!='#':
            nbi+=1
            if board[nbi][bj]=='O':
                flag=1
    
    if flag==2 and count<10:
        print(count+1)
        break
    if flag==0 and (nri!=ri or nbi!=bi):
        stack.append([[nri,rj],[nbi,bj],count+1,s+'d'])
    
    #왼쪽
    flag=0
    nri,nrj,nbi,nbj=ri,rj,bi,bj
    if ri==bi:
        if rj<bj:
            while board[ri][nrj-1]!='#':
                nrj-=1
                if board[ri][nrj]=='O':
                    flag=2
            if flag==2:
                nrj-=1
            while board[bi][nbj-1]!='#' and nbj-1>nrj:
                nbj-=1
                if board[bi][nbj]=='O':
                    flag=1
        else:
            while board[bi][nbj-1]!='#':
                nbj-=1
                if board[bi][nbj]=='O':
                    flag=1
            while board[ri][nrj-1]!='#' and nrj-1>nbj:
                nrj-=1
                if flag!=1 and board[ri][nrj]=='O':
                    flag=2
    else:
        while board[ri][nrj-1]!='#':
            nrj-=1
            if board[ri][nrj]=='O':
                flag=2
        while board[bi][nbj-1]!='#':
            nbj-=1
            if board[bi][nbj]=='O':
                flag=1
    
    if flag==2 and count<10:
        print(count+1)
        break
    if flag==0 and (nrj!=rj or nbj!=bj):
        stack.append([[ri,nrj],[bi,nbj],count+1,s+'l'])
    
if flag!=2:
    print(-1)
