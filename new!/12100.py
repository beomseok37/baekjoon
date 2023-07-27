def recursion(nowBoard,count):
    global N,answer
    
    if count==5:
        for i in range(N):
            answer = max(answer,max(nowBoard[i]))
        return
    
    temp = [nowBoard[i][:] for i in range(N)]
    i=0
    while i<N:
        j,k=0,1 # j가 숫자가 놓일 장소, k가 숫자 가져올 장소
        while k<N:
            if temp[i][j]==0:
                if temp[i][k]!=0:
                    temp[i][j]=temp[i][k]
                temp[i][k]=0
            elif temp[i][j]==temp[i][k]:
                temp[i][j]*=2
                j+=1
                temp[i][k]=0
            else:
                if temp[i][k]!=0:
                    j+=1
                    temp[i][j]=temp[i][k]
                    if j!=k:
                        temp[i][k]=0
            k+=1
        i+=1
    recursion(temp,count+1)
    
    temp = [nowBoard[i][:] for i in range(N)]
    j=0
    while j<N:
        i,k=0,1 # i가 숫자가 놓일 장소, k가 숫자 가져올 장소
        while k<N:
            if temp[i][j]==0:
                if temp[k][j]!=0:
                    temp[i][j]=temp[k][j]
                temp[k][j]=0
            elif temp[i][j]==temp[k][j]:
                temp[i][j]*=2
                i+=1
                temp[k][j]=0
            else:
                if temp[k][j]!=0:
                    i+=1
                    temp[i][j]=temp[k][j]
                    if i!=k:
                        temp[k][j]=0
            k+=1
        j+=1
    recursion(temp,count+1)
    
    temp = [nowBoard[i][:] for i in range(N)]
    i=N-1
    while i>=0:
        j,k=N-1,N-2 # j가 숫자가 놓일 장소, k가 숫자 가져올 장소
        while k>=0:
            if temp[i][j]==0:
                if temp[i][k]!=0:
                    temp[i][j]=temp[i][k]
                temp[i][k]=0
            elif temp[i][j]==temp[i][k]:
                temp[i][j]*=2
                j-=1
                temp[i][k]=0
            else:
                if temp[i][k]!=0:
                    j-=1
                    temp[i][j]=temp[i][k]
                    if j!=k:
                        temp[i][k]=0
            k-=1
        i-=1
    recursion(temp,count+1)
    
    temp = [nowBoard[i][:] for i in range(N)]
    j=N-1
    while j>=0:
        i,k=N-1,N-2 # i가 숫자가 놓일 장소, k가 숫자 가져올 장소
        while k>=0:
            if temp[i][j]==0:
                if temp[k][j]!=0:
                    temp[i][j]=temp[k][j]
                temp[k][j]=0
            elif temp[i][j]==temp[k][j]:
                temp[i][j]*=2
                i-=1
                temp[k][j]=0
            else:
                if temp[k][j]!=0:
                    i-=1
                    temp[i][j]=temp[k][j]
                    if i!=k:
                        temp[k][j]=0
            k-=1
        j-=1
    recursion(temp,count+1)
    
            

N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
answer=0

recursion(board,0)
print(answer)
