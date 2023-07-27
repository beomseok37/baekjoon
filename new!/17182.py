def recursion(pos, count, total):
    global result

    if count == N:
        result = min(result, total)
        return

    for num in range(N):
        if not visited[num]:
            visited[num] = True
            recursion(num, count + 1, total + T[pos][num])
            visited[num] = False
            
N,K=list(map(int,input().split()))
T=[list(map(int,input().split())) for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            T[i][j] = min(T[i][j], T[i][k] + T[k][j])

visited=[False for _ in range(N)]
visited[K]=True
result=float("inf")
recursion(K,1,0)
print(result)
