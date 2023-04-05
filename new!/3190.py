import sys
input = sys.stdin.readline

N=int(input())
K=int(input())
apples=[list(map(int,input().split())) for _ in range(K)]
L=int(input())
changes=[input().split() for _ in range(L)]
board=[[0 for _ in range(N+2)] for __ in range(N+2)]
head,tail=[1,1],[1,1]
curves=[]

for r,c in apples:
    board[r][c]=1

board[1][1]=2
time=0
direction=1 # 0:위 1:오 2:아 3:왼
c_i=0
while 0<head[0]<=N and 0<head[1]<=N:
    time+=1
    
    if direction==0:
        head[0]-=1
    elif direction==1:
        head[1]+=1
    elif direction==2:
        head[0]+=1
    else:
        head[1]-=1
    
    if board[head[0]][head[1]]==2:
        break
    if not (0<head[0]<=N and 0<head[1]<=N):
        break
    
    if board[head[0]][head[1]]==0:
        board[tail[0]][tail[1]]=0
        if curves and tail[0]==curves[0][0] and tail[1]==curves[0][1]:
            curves.pop(0)
            
        if curves:
            if curves[0][0]==tail[0]:
                tail[1]+= 1 if curves[0][1]>tail[1] else -1
            else:
                tail[0]+= 1 if  curves[0][0]>tail[0] else -1
        else:
            if head[0]==tail[0]:
                tail[1]+= 1 if head[1]>tail[1] else -1
            else:
                tail[0]+= 1 if head[0]>tail[0] else -1
    
    board[head[0]][head[1]]=2
    
    if c_i<L and changes[c_i][0]==str(time):
        if changes[c_i][1]=='L':
            direction= direction-1 if direction>0 else 3
        else:
            direction= (direction+1)%4
        curves.append([head[0],head[1]])
        c_i+=1
print(time)
