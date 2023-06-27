def change_direction(d):
    return d if d>=0 else 4+d
def back_direction(d):
    return d-2 if d>1 else 2+d
def check(r,c,d):
    global N,M
    if d==0 and r>0:
        return [r-1,c]
    elif d==1 and c<M-1:
        return [r,c+1]
    elif d==2 and r<N-1:
        return [r+1,c]
    elif d==3 and c>0:
        return [r,c-1]
    return [-1,-1]

N,M=list(map(int,input().split()))
r,c,d=list(map(int,input().split()))
board=[list(map(int,input().split())) for _ in range(N)]
board[r][c],count=2,1
stack=[[r,c,d]]
while stack:
    r,c,d=stack.pop()
    
    for i in range(1,5):
        new_d=change_direction(d-i)
        new_r,new_c = check(r,c,new_d)
        if new_r!=-1 and board[new_r][new_c]==0:    
            board[new_r][new_c]=2
            count+=1
            stack.append([new_r,new_c,new_d])
            break
    else:
        back_d=back_direction(d)
        back_r,back_c=check(r,c,back_d)
        if back_r==-1 or board[back_r][back_c]==1:
            break
        else:
            stack.append([back_r,back_c,d])
        
print(count)
