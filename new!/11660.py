import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))
array = [list(map(int, input().split())) for _ in range(N)]
checkList = [list(map(lambda x: int(x)-1, input().split())) for _ in range(M)]
prefixArray = [[array[i][0]] for i in range(N)]

for i in range(N):
    for j in range(1, N):
        prefixArray[i].append(prefixArray[i][-1]+array[i][j])

for x1, y1, x2, y2 in checkList:
    answer = 0
    for x in range(x1, x2+1):
        answer += prefixArray[x][y2]-prefixArray[x][y1]+array[x][y1]
    print(answer)
