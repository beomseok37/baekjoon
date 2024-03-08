from heapq import heappush, heappop


N = int(input())
lectures = [list(map(int, input().split())) for _ in range(N)]
lectures.sort()
classRoom = []
heappush(classRoom, lectures[0][1])

for i in range(1, N):
    if classRoom[0] <= lectures[i][0]:
        heappop(classRoom)
    heappush(classRoom, lectures[i][1])

print(len(classRoom))
