from heapq import heappush, heappop
from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input())
lectures = sorted([list(map(int, input().split()))
                  for _ in range(N)], key=lambda x: x[1])
answer = []

for p, d in lectures:
    heappush(answer, p)
    if len(answer) > d:
        heappop(answer)
print(sum(answer))
