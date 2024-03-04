import sys
import math
input = sys.stdin.readline


def minInit(start, end, node):
    if start == end:
        minSegTree[node] = A[start]
        return minSegTree[node]

    mid = (start+end)//2
    minSegTree[node] = min(minInit(start, mid, node*2),
                           minInit(mid+1, end, node*2+1))
    return minSegTree[node]


def minFind(start, end, left, right, node):
    if start > right or end < left:
        return 1_000_000_001
    if left <= start and end <= right:
        return minSegTree[node]

    mid = (start+end)//2
    return min(minFind(start, mid, left, right, node*2), minFind(mid+1, end, left, right, node*2+1))


def maxInit(start, end, node):
    if start == end:
        maxSegTree[node] = A[start]
        return maxSegTree[node]

    mid = (start+end)//2
    maxSegTree[node] = max(maxInit(start, mid, node*2),
                           maxInit(mid+1, end, node*2+1))
    return maxSegTree[node]


def maxFind(start, end, left, right, node):
    if start > right or end < left:
        return 0
    if left <= start and end <= right:
        return maxSegTree[node]

    mid = (start+end)//2
    return max(maxFind(start, mid, left, right, node*2), maxFind(mid+1, end, left, right, node*2+1))


N, M = list(map(int, input().split()))
A = [int(input()) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(M)]
dataSize = 2**(math.ceil(math.log2(N))+1)
minSegTree = [0 for _ in range(dataSize)]
maxSegTree = [0 for _ in range(dataSize)]
minInit(0, N-1, 1)
maxInit(0, N-1, 1)
for a, b in B:
    print(minFind(0, N-1, a-1, b-1, 1), maxFind(0, N-1, a-1, b-1, 1))
