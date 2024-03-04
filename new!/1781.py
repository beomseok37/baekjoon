from queue import PriorityQueue
import sys
input = sys.stdin.readline

N = int(input())
problems = [list(map(int, input().split())) for _ in range(N)]
answer = 0
pq = PriorityQueue()
problems.sort(key=lambda x: (-x[0], -x[1]))

j = 0
for i in range(N, 0, -1):
    while j < N and problems[j][0] == i:
        pq.put((-problems[j][1], problems[j][0]))
        j += 1

    while not pq.empty():
        temp = pq.get()
        if temp[1] >= i:
            answer += -temp[0]
            break
print(answer)
