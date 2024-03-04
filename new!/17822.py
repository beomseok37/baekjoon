N, M, T = list(map(int, input().split()))
plates = [list(map(int, input().split())) for _ in range(N)]
rotates = [list(map(int, input().split())) for _ in range(T)]


def rotateRight(i, k):
    temp = plates[i][:]
    for j in range(M):
        plates[i][j] = temp[j-k] if j-k >= 0 else temp[M+(j-k)]


def rotateLeft(i, k):
    temp = plates[i][:]
    for j in range(M):
        plates[i][j] = temp[j+k] if j+k < M else temp[j+k-M]


for x, d, k in rotates:
    for i in range(x, N+1, x):
        if d == 0:
            rotateRight(i-1, k)
        else:
            rotateLeft(i-1, k)

    remove = []
    temp = []
    for i in range(M):
        curr = plates[0][i]
        flag = False
        temp.append([0, i])
        for j in range(1, N):
            if curr == plates[j][i]:
                flag = True
                temp.append([j, i])
            else:
                curr = plates[j][i]
                if not flag:
                    temp.pop()
                flag = False
                temp.append([j, i])

        if not flag:
            temp.pop()

    for i, j in temp:
        if plates[i][j] != 0:
            remove.append([i, j])
    temp = []
    for i in range(N):
        curr = plates[i][-1]
        temp.append([i, M-1])
        flag = False
        flag2 = False
        for j in range(M):
            if curr == plates[i][j]:
                flag = True
                if j == M-1 and flag2:
                    continue
                if j == 0:
                    flag2 = True

                temp.append([i, j])
            else:
                curr = plates[i][j]
                if not flag:
                    temp.pop()
                flag = False
                temp.append([i, j])

        if not flag:
            temp.pop()

    for i, j in temp:
        if plates[i][j] != 0:
            remove.append([i, j])

    if len(remove) == 0:
        total = 0
        count = 0
        for i in range(N):
            for j in range(M):
                total += plates[i][j]
                if plates[i][j] != 0:
                    count += 1
        if count == 0:
            break
        total = total/count

        for i in range(N):
            for j in range(M):
                if plates[i][j] == 0 or plates[i][j] == total:
                    continue

                plates[i][j] = plates[i][j] - \
                    1 if plates[i][j] > total else plates[i][j]+1
    else:
        for i, j in remove:
            plates[i][j] = 0
answer = 0
for i in range(N):
    answer += sum(plates[i])
print(answer)
