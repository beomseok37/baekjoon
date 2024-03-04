# 얻을 수 있는 점수의 크기를 최대로
# 각 문제를 풀었을 때 점수를 얻을 수 있고
# 각 문제는 기한이 있다

from heapq import heappush, heappop
N = int(input())
works = [list(map(int, input().split())) for _ in range(N)]

works.sort()
queue = []

answer = 0
for i in range(N, 0, -1):
    while works and works[-1][0] >= i:
        heappush(queue, -works.pop()[1])

    if queue:
        answer -= heappop(queue)
print(answer)
