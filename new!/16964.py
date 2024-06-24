from collections import deque, defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
edges = defaultdict(list)
for _ in range(N-1):
    a, b = list(map(int, input().split()))
    edges[a].append(b)
    edges[b].append(a)
answer = deque(list(map(int, input().split())))
cur_i = 0


def dfs(ans):
    tmp = ans.popleft()
    if not ans:
        print(1)
        exit(0)
    flag = ans[0] in edges[tmp]
    for _ in range(len(edges[tmp])):
        if flag:
            dfs(ans)


if answer[0] != 1:
    print(0)
    exit(0)

dfs(answer)
print(0)
