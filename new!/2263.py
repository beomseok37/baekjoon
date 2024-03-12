import sys
sys.setrecursionlimit(10 ** 6)

N = int(input())
inOrder = list(map(int, input().split()))
postOrder = list(map(int, input().split()))
inOrderDict = {}
result = []
for i in range(N):
    inOrderDict[inOrder[i]] = i


def findPreOrder(inStart, inEnd, postStart, postEnd):
    if inStart > inEnd or postStart > postEnd:
        return

    root = postOrder[postEnd]
    leftCount = inOrderDict[root]-inStart
    rightCount = inEnd - inOrderDict[root]

    result.append(root)

    findPreOrder(inStart, inStart+leftCount-1,
                 postStart, postStart+leftCount-1)
    findPreOrder(inEnd - rightCount + 1, inEnd, postEnd-rightCount, postEnd-1)


findPreOrder(0, N-1, 0, N-1)
print(' '.join(map(str, result)))
