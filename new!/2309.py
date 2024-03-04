heights = sorted([[int(input()), i] for i in range(9)])
overHeight = sum(map(lambda x: x[0], heights))-100
lier = [-1, -1]

for i in range(8):
    for j in range(i+1, 9):
        if heights[i][0]+heights[j][0] == overHeight:
            lier[0] = heights[i][1]
            lier[1] = heights[j][1]
            break
    if lier[0] != -1:
        break

for height, i in heights:
    if i == lier[0] or i == lier[1]:
        continue
    print(height)
