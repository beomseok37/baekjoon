from heapq import heappush, heappop

N = int(input())
flowers = []

for _ in range(N):
    sm, sd, em, ed = list(map(int, input().split()))
    flowers.append([sm*100+sd, em*100+ed])
flowers.sort()

selected = []
si = 0
now = 301
answer = 0

while now <= 1130:
    for i in range(si, N):
        if flowers[i][0] <= now < flowers[i][1]:
            heappush(selected, -flowers[i][1])
            si = i+1
        elif flowers[i][0] > now:
            break

    if selected:
        now = -heappop(selected)
        answer += 1
        selected = []
    else:
        break
if now > 1130:
    print(answer)
else:
    print(0)
