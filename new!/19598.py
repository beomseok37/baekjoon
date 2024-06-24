import sys
from heapq import heappush, heappop
input = sys.stdin.readline
N = int(input())
classes = [list(map(int, input().split())) for _ in range(N)]
classes.sort()

heap = []
heappush(heap, classes[0][1])
for i in range(1, N):
    minClass = heappop(heap)
    if minClass > classes[i][0]:
        heappush(heap, minClass)
    heappush(heap, classes[i][1])
print(len(heap))
