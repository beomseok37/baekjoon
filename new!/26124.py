import sys
input = sys.stdin.readline

H,W = list(map(int,input().split()))
visited=[[False for _ in range(W+2)] for __ in range(H+2)]
h=[-1,0,0,1]
w=[0,-1,1,0]
room = []
count=0
miro = [[-1 for _ in range(W+2)]]

for i in range(H):
    temp = list(map(int,input().split()))
    for j in range(W):
        room.append([i+1,j+1])
    miro.append([-1]+temp+[-1])
miro.append([-1 for _ in range(W+2)])

room.sort(key=lambda x:miro[x[0]][x[1]],reverse=True)

flag=True
for height,width in room:
    brightness = miro[height][width]
    if visited[height][width] or brightness==0 or brightness==-1:
        continue
    
    count+=1
    if brightness==1:
        continue
    
    queue = [[height,width]]
    while queue:
        c_h,c_w=queue.pop(0)
        c_b = miro[c_h][c_w]
        
        if c_b==1:
            continue
        
        for i in range(4):
            n_h,n_w=c_h+h[i],c_w+w[i]
            n_b=miro[n_h][n_w]
            
            if n_b==-1:
                continue
            
            if c_b-n_b==1:
                if not visited[n_h][n_w]:
                    queue.append([n_h,n_w])
                    visited[n_h][n_w]=True
            elif c_b-n_b>1:
                flag=False
                break
                
        if not flag:
            break
    
    if not flag:
        break
    
print(count if flag else -1)
