import sys
input = sys.stdin.readline

def get_next(pos):
    result=[]
    y=[-2,-2,-1,-1,1,1,2,2]
    x=[-1,1,-2,2,-2,2,-1,1]
    for i in range(8):
        result.append([pos[0],pos[1]+y[i],pos[2]+x[i]])
    return result

def find(index,total,number,count):
    global N,M,answer
    if number>count:
        temp=knight[index]
        next_pos=get_next(knight[index])
        for i in range(len(next_pos)):
            if 0<=next_pos[i][1]<N and 0<=next_pos[i][2]<M and not visited[next_pos[i][0]-1][next_pos[i][1]][next_pos[i][2]]:
                knight[index]=next_pos[i]
                visited[knight[index][0]-1][knight[index][1]][knight[index][2]] = True
                find(index,total,number,count+1)
                visited[knight[index][0]-1][knight[index][1]][knight[index][2]] = False
                knight[index]=temp
    else:
        total+=1
        count=0
        pos=knight[0]
        for i in range(1,len(knight)):
            if pos[1]!=knight[i][1] or pos[2]!=knight[i][2]:
                break
        else:
            print(knight,total)
            answer=min(answer,total)
            return
        
        for i in range(len(knight)):
            next_pos=get_next(knight[i])
            temp = knight[i]
            for j in range(len(next_pos)):
                if 0<=next_pos[j][1]<N and 0<=next_pos[j][2]<M and not visited[next_pos[j][0]-1][next_pos[j][1]][next_pos[j][2]]:
                    knight[i]=next_pos[j]
                    visited[knight[i][0]-1][knight[i][1]][knight[i][2]] = True
                    find(i,total,knight[i][0],count+1)
                    visited[knight[i][0]-1][knight[i][1]][knight[i][2]] = False
                    knight[i]=temp

N,M=list(map(int,input().split()))
chess=[]
knight=[]
answer=1000000
visited=[[[False for _ in range(M)] for __ in range(N)] for ___ in range(9)]
for i in range(N):
    temp=list(input())[:-1]
    chess.append(temp)
    for j in range(M):
        if temp[j]!='.':
            knight.append([int(temp[j]),i,j])
            visited[int(temp[j])-1][i][j]=True

find(0,-1,0,0)
print(answer)
