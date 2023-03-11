import sys
import heapq
input = sys.stdin.readline

N=int(input())
grid=[list(map(int,input().split())) for _ in range(N)]
visited=[[sys.maxsize for _ in range(N)] for __ in range(N)]
row_move=[-1,0,0,1]
column_move=[0,1,-1,0]

queue=[]
visited[0][0]=0
heapq.heappush(queue,(0,0,0))
while queue:
    max_slope,r,c=heapq.heappop(queue)
    
    if visited[r][c]<max_slope:
        continue
    
    for i in range(4):
        next_r=r+row_move[i]
        next_c=c+column_move[i]
        
        if 0<=next_r<=N-1 and 0<=next_c<=N-1:
            new_max_slope=max(max_slope,abs(grid[r][c]-grid[next_r][next_c]))
            if new_max_slope<visited[next_r][next_c]:
                visited[next_r][next_c]=new_max_slope
                heapq.heappush(queue,(new_max_slope,next_r,next_c))
print(visited[N-1][N-1])
