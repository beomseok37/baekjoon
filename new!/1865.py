from collections import deque
import sys
input = sys.stdin.readline


def bellmanFord():
    distance = [sys.maxsize for _ in range(N+1)]
    distance[1] = 0
    for i in range(N):
        for start, end, length in edges:
            if distance[end] > distance[start]+length:
                distance[end] = distance[start]+length

                if i == N-1:
                    return 'YES'
    return 'NO'


test_count = int(input())
for _ in range(test_count):
    N, M, W = list(map(int, input().split()))
    edges = []
    for _ in range(M):
        S, E, T = list(map(int, input().split()))
        edges.append((S, E, T))
        edges.append((E, S, T))

    for _ in range(W):
        S, E, T = list(map(int, input().split()))
        edges.append((S, E, -T))

    print(bellmanFord())
