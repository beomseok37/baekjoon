N=int(input())
weights = list(map(int,input().split()))
weights.sort()

answer=1
for i in range(N):
    if answer<weights[i]:
        break
    answer+=weights[i]
print(answer)
