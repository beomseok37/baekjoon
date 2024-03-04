from collections import defaultdict
import copy
import sys
input=sys.stdin.readline

def move(x,y,count,fishCount,path):
    global maxFishCount,maxPath
    if count==3:
        if maxFishCount<fishCount:
            maxPath=path[:]
            maxFishCount=fishCount
        return
            
    for i in range(4):
        nx,ny=x+wizardDirection[i][0],y+wizardDirection[i][1]
        
        if not (1<=nx<=4 and 1<=ny<=4):
            continue
        
        newPath=path[:]
        newPath.append((wizardDirection[i][0],wizardDirection[i][1]))
        
        if visited[nx][ny]:
            move(nx,ny,count+1,fishCount,newPath)
        else:
            visited[nx][ny]=True
            move(nx,ny,count+1,fishCount+len(fishMaps[(nx,ny)]),newPath)
            visited[nx][ny]=False
        
M,S=list(map(int,input().split()))
fishList=[list(map(int,input().split())) for _ in range(M)]
wizard = list(map(int,input().split()))
fishDirection = [(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0)]
wizardDirection = [(-1,0),(0,-1),(1,0),(0,1)]
smellMaps = [[-1 for _ in range(6)] for __ in range(6)] # -1 빈곳, -2:위자드, 양수: 물고기냄새 사라지는 턴
wizardMaps = [[-1 for _ in range(6)] for __ in range(6)] # -1 빈곳, -2:위자드, 양수: 물고기냄새 사라지는 턴
visited=[[False for _ in range(6)] for __ in range(6)]
fishMaps = defaultdict(list)
wizardMaps[wizard[0]][wizard[1]]=-2

for fx,fy,d in fishList:
    fishMaps[(fx,fy)].append(d%8)

for turn in range(S):
    #1
    copiedMaps=copy.deepcopy(fishMaps)
    #2
    
    newFishMap=defaultdict(list)
    for (i,j),dList in fishMaps.items():
        for od in dList:
            nx,ny,d=0,0,od
            for k in range(8):
                nx,ny=i+fishDirection[d][0],j+fishDirection[d][1]
                
                if not (1<=nx<=4 and 1<=ny<=4) or turn<=smellMaps[nx][ny] or wizardMaps[nx][ny]==-2:
                    d=d-1 if d-1>=0 else 7
                    continue
                fishMaps[(nx,ny)].append(d)
                break        
            else:
                fishMaps[(i,j)].remove(od)
                continue
            
    fishMaps=copy.deepcopy(newFishMap)

    #3
    maxPath=[]
    maxFishCount=-1
    move(wizard[0],wizard[1],0,0,[])
    
    nx,ny=wizard
    wizardMaps[nx][ny]=-1
    for dx,dy in maxPath:
        nx+=dx
        ny+=dy
        if len(fishMaps[(nx,ny)])>0:
            smellMaps[nx][ny]=turn+2
            fishMaps[(nx,ny)].clear()
    wizard[0],wizard[1]=nx,ny
    wizardMaps[nx][ny]=-2
    
    #5
    for pos,dList in copiedMaps.items():
        fishMaps[pos].extend(dList)
                
answer=0
for pos,dList in fishMaps.items():
    answer+=len(dList)
print(answer)
