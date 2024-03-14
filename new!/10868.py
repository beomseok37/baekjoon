import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))
arr = [int(input()) for _ in range(N)]
ranges = [list(map(int, input().split())) for _ in range(M)]
nodes = [sys.maxsize for _ in range(N*4)]


def init(start, end, index):
    if start == end:
        nodes[index] = arr[start]
    else:
        mid = (start+end)//2
        nodes[index] = min(init(start, mid, index*2),
                           init(mid+1, end, index*2+1))
    return nodes[index]


def findMin(fullRangeStart, fullRangeEnd, rangeStart, rangeEnd, index):
    if fullRangeStart > rangeEnd or fullRangeEnd < rangeStart:
        return sys.maxsize
    elif fullRangeStart <= rangeStart and fullRangeEnd >= rangeEnd:
        return nodes[index]
    else:
        mid = (rangeStart+rangeEnd)//2
        return min(findMin(fullRangeStart, fullRangeEnd, rangeStart, mid, index*2), findMin(fullRangeStart, fullRangeEnd, mid+1, rangeEnd, index*2+1))


init(0, N-1, 1)
for fullRangeStart, fullRangeEnd in ranges:
    print(findMin(fullRangeStart-1, fullRangeEnd-1, 0, N-1, 1))
