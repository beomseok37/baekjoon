from heapq import heapify, heappush, heappop

T = int(input())
for _ in range(T):
    K = int(input())
    files = list(map(int, input().split()))
    heapify(files)
    answer = 0
    while len(files) > 1:
        minValue1 = heappop(files)
        minValue2 = heappop(files)
        temp = minValue1+minValue2
        answer += temp
        heappush(files, temp)

    print(answer)
