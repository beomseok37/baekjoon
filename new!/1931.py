N=int(input())
meeting=[list(map(int,input().split())) for _ in range(N)]

meeting.sort(key=lambda x:(x[1],x[0]))

count=1
time=meeting[0][1]
for i in range(1,N):
    if meeting[i][0]>=time:
        count+=1
        time=meeting[i][1]
print(count)
