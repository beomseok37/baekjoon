N, K = list(map(int, input().split()))
board = list(map(int, input().split()))
count = 0
# 확인

while True:
    maxValue, minValue = 0, 10_001
    for fish in board:
        maxValue = max(maxValue, fish)
        minValue = min(minValue, fish)

    if maxValue-minValue <= K:
        break

    # 분배
    minList = [0]
    for i in range(1, N):
        if board[minList[0]] > board[i]:
            minList.clear()
            minList.append(i)
        elif board[minList[0]] == board[i]:
            minList.append(i)

    for minIndex in minList:
        board[minIndex] += 1

    # 쌓아 올리기
    dummy = [[board[0]], board[1:]]
    while len(dummy) <= (len(dummy[-1])-len(dummy[0])):
        temp = [[] for _ in range(len(dummy[0]))]
        for i in range(len(dummy[0])):
            for j in range(len(dummy)):
                temp[i].append(dummy[len(dummy)-1-j][i])
        temp.append(dummy[-1][len(dummy[0]):])
        dummy = [tempValue[:] for tempValue in temp]
    # 분배
    share = []
    for i in range(len(dummy)):
        for j in range(len(dummy[i])):
            if i+1 < len(dummy):
                difference = abs(dummy[i][j]-dummy[i+1][j])

                if difference >= 5:
                    if dummy[i][j] > dummy[i+1][j]:
                        share.append((i, j, -(difference//5)))
                        share.append((i+1, j, difference//5))
                    if dummy[i][j] < dummy[i+1][j]:
                        share.append((i, j, difference//5))
                        share.append((i+1, j, -(difference//5)))
            if j+1 < len(dummy[i]):
                difference = abs(dummy[i][j]-dummy[i][j+1])

                if difference >= 5:
                    if dummy[i][j] > dummy[i][j+1]:
                        share.append((i, j, -(difference//5)))
                        share.append((i, j+1, difference//5))
                    if dummy[i][j] < dummy[i][j+1]:
                        share.append((i, j, difference//5))
                        share.append((i, j+1, -(difference//5)))
    for i, j, num in share:
        dummy[i][j] += num
    # 다시 풀기
    board = []
    for i in range(len(dummy[0])):
        for j in range(len(dummy)):
            board.append(dummy[len(dummy)-1-j][i])
    board.extend(dummy[-1][len(dummy[0]):])
    # 반 접어 올리기
    temp = [[board[i] for i in range(len(board)//2-1, -1, -1)],
            [board[i+len(board)//2] for i in range(len(board)//2)]]
    dummy = [[], [], [], []]
    for i in range(len(temp[0])//2):
        dummy[0].append(temp[1][len(temp[0])//2-1-i])
        dummy[1].append(temp[0][len(temp[0])//2-1-i])
        dummy[2].append(temp[0][len(temp[0])//2+i])
        dummy[3].append(temp[1][len(temp[0])//2+i])
    # 분배
    share = []
    for i in range(len(dummy)):
        for j in range(len(dummy[i])):
            if i+1 < len(dummy):
                difference = abs(dummy[i][j]-dummy[i+1][j])

                if difference >= 5:
                    if dummy[i][j] > dummy[i+1][j]:
                        share.append((i, j, -(difference//5)))
                        share.append((i+1, j, difference//5))
                    if dummy[i][j] < dummy[i+1][j]:
                        share.append((i, j, difference//5))
                        share.append((i+1, j, -(difference//5)))
            if j+1 < len(dummy[i]):
                difference = abs(dummy[i][j]-dummy[i][j+1])

                if difference >= 5:
                    if dummy[i][j] > dummy[i][j+1]:
                        share.append((i, j, -(difference//5)))
                        share.append((i, j+1, difference//5))
                    if dummy[i][j] < dummy[i][j+1]:
                        share.append((i, j, difference//5))
                        share.append((i, j+1, -(difference//5)))
    for i, j, num in share:
        dummy[i][j] += num
    # 다시 풀기
    board = []
    for i in range(len(dummy[0])):
        for j in range(len(dummy)):
            board.append(dummy[len(dummy)-1-j][i])
    count += 1
print(count)
