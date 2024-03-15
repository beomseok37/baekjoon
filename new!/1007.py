from itertools import combinations
from math import sqrt
import sys
input = sys.stdin.readline


def init():
    N = int(input())
    points = []
    for __ in range(N):
        points.append(list(map(int, input().split())))
    return [N, points]


def findMin(N, points):
    result = sys.maxsize

    combiList = list(combinations(range(N), N//2))
    for i in range(len(combiList)//2):
        plusIndexes = combiList[i]
        plus, minus = [0, 0], [0, 0]
        visited = [False for _ in range(N)]
        for i in plusIndexes:
            visited[i] = True
            plus[0] += points[i][0]
            plus[1] += points[i][1]

        for i in range(N):
            if visited[i]:
                continue
            minus[0] += points[i][0]
            minus[1] += points[i][1]

        result = min(result, sqrt((plus[0]-minus[0])**2+(plus[1]-minus[1])**2))

    return result


T = int(input())
for _ in range(T):
    N, points = init()
    result = findMin(N, points)
    print(result)
