import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
edges = [list(map(int, input().split())) for _ in range(N)]
childCount = [[0, 0] for _ in range(N)]


def init(node):
    print(node)
    if edges[node-1][1] != -1:
        childCount[node-1][0] = init(edges[node-1][1])
    if edges[node-1][2] != -1:
        childCount[node-1][1] = init(edges[node-1][2])
    return sum(childCount[node-1])+1


init(1)
answer = 0
answerLength = 0
stack = [[1]]
step = 1
while stack:
    children = stack.pop()

    if not children:
        break

    s, e = children[0], children[-1]
    length = childCount[s][1]+childCount[e][0]+3
    if answerLength < length:
        answer = step

    newChildren = []
    for child in children:
        if edges[child][1] != -1:
            newChildren.append(edges[child][1])
        if edges[child][2] != -1:
            newChildren.append(edges[child][2])
    stack.append(children)
print(answer)
