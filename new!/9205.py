from collections import deque

T=int(input())
for t in range(T):
    n=int(input())
    home=list(map(int,input().split()))
    shop=[list(map(int,input().split())) for _ in range(n)]
    party=list(map(int,input().split()))
    visited=[False for _ in range(n)]

    flag=False
    queue=deque()
    queue.append(home[:])
    while queue:
        x,y=queue.popleft()
        if abs(x-party[0])+abs(y-party[1])<=1000:
            flag=True
            break

        for i in range(n):
            if abs(x-shop[i][0])+abs(y-shop[i][1])>1000:
                continue

            if not visited[i]:
                visited[i]=True
                queue.append(shop[i][:])

    print('happy' if flag else 'sad')
