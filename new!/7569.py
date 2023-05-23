from collections import deque

def change(string):
    return int(string)-1

m,n,h=list(map(int,input().split()))
tomato=[]
for i in range(h):
    temp=[]
    for j in range(n):
        temp.append(list(map(change,input().split())))
    tomato.append([temp[k][:] for k in range(n)])

dx=[-1,1,0,0,0,0]
dy=[0,0,-1,1,0,0]
dz=[0,0,0,0,-1,1]
answer=-1

queue=deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k]==0:
                queue.append([k,j,i,0])

while queue:
    x, y, z, day = queue.popleft()

    for l in range(6):
        nx = x + dx[l]
        ny = y + dy[l]
        nz = z + dz[l]

        if not (0 <= nx < m and 0 <= ny < n and 0 <= nz < h):
            continue

        if tomato[nz][ny][nx] == -1:
            tomato[nz][ny][nx] = day + 1
            queue.append([nx, ny, nz, day + 1])

for i in range(h):
    for j in range(n):
        for k in range(m):
            answer=max(answer,tomato[i][j][k])
            if tomato[i][j][k]==-1:
                print(-1)
                exit()
print(answer)
