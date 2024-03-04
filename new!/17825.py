dices = list(map(int, input().split()))
score = [i*2 for i in range(20)]
score.extend([13, 16, 19, 22, 24, 28, 27, 26, 25, 30, 35, 40, 0])
length = 33
answer = 0


def getStartPos(pos):
    if pos == 5:
        return 19
    elif pos == 10:
        return 22
    elif pos == 15:
        return 24
    else:
        return pos


def dfs(i, total, horse):
    global answer
    if i == 10:
        answer = max(answer, total)
        return

    dice = dices[i]

    for j in range(4):
        pos = horse[j]
        startPos = getStartPos(pos)
        newPos = startPos+dice
        if (pos == 5 or 20 <= pos <= 22) and newPos > 22:
            newPos += 5
        elif (pos == 10 or 23 <= pos <= 24) and newPos > 24:
            newPos += 3
        elif 16 <= pos <= 19 and newPos > 19:
            newPos += 11

        if newPos > 32:
            newPos = 32

        if newPos != 32 and newPos in horse:
            continue

        newTotal = total+score[newPos]
        newHorse = horse[:]
        newHorse[j] = newPos

        dfs(i+1, newTotal, newHorse)


dfs(0, 0, [0, 0, 0, 0])
print(answer)
