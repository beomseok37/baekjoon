import sys
input = sys.stdin.readline

N,M,K,X = list(map(int,input().split()))
roads = [[] for _ in range(N+1)]

for i in range(M):
    A,B = list(map(int,input().split()))
    roads[A].append(B)

result = []
queue=[[0,X]] # count, position
visited=[False for _ in range(N+1)]
visited[X] = True
while queue:
    count, position = queue.pop(0)
    
    if count != K:
        for next_position in roads[position]:
            if not visited[next_position]:
                queue.append([count+1,next_position])
                visited[next_position] = True
    else:
        result.append(position)
        
print(' '.join(map(str,sorted(result))) if result else -1)
