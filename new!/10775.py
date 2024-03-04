from heapq import heappush, heappop
G, P = int(input()), int(input())
g = [int(input()) for _ in range(P)]
root = [i for i in range(G+1)]


def find(num):
    if root[num] == num:
        return num

    root[num] = find(root[num])
    return root[num]


def union(a, b):
    rootA = find(a)
    rootB = find(b)
    root[rootA] = rootB


answer = 0
for i in range(P):
    rootG = find(g[i])

    if rootG == 0:
        break

    union(rootG, rootG-1)
    answer += 1
print(answer)
