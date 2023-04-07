def roll(dice,direction):
    if direction==1:
        dice[0],dice[1],dice[2],dice[5]=dice[1],dice[5],dice[0],dice[2]
    elif direction==2:
        dice[0],dice[1],dice[2],dice[5]=dice[2],dice[0],dice[5],dice[1]
    elif direction==3:
        dice[0],dice[3],dice[4],dice[5]=dice[3],dice[5],dice[0],dice[4]
    else:
        dice[0],dice[3],dice[4],dice[5]=dice[4],dice[0],dice[5],dice[3]
    return dice

N,M,x,y,K=list(map(int,input().split()))
board=[list(map(int,input().split())) for _ in range(N)]
orders=list(map(int,input().split())) # 동: 1 서:2 북:3 남:4
dice=[0 for _ in range(6)]
now=0

for order in orders:
    flag=True
    if order==1 and y+1<M:
        y+=1
        flag=False
    elif order==2 and y-1>=0:
        y-=1
        flag=False
    elif order==3 and x-1>=0:
        x-=1
        flag=False
    elif order==4 and x+1<N:
        x+=1
        flag=False
    
    if flag:
        continue
    
    dice=roll(dice[:],order)
    if board[x][y]==0:
        board[x][y]=dice[0]
    else:
        dice[0]=board[x][y]
        board[x][y]=0
    print(dice[5])
    