row, column = list(map(int,input().split(' ')))
chess = []
for i in range(row):
  chess.append(list(input()))

answer = 64
flag = True

for rowStart in range(row-7):
  for columnStart in range(column-7):
    temp = 0
    for i in range(rowStart,rowStart+8):
      for j in range(columnStart,columnStart+8): 
        if flag:
          if j % 2 ==0:
            if chess[i][j] == 'B':
              temp += 1
          else:
            if chess[i][j] == 'W':
              temp += 1
        else:
          if j % 2 ==0:
            if chess[i][j] == 'W':
              temp += 1
          else:
            if chess[i][j] == 'B':
              temp += 1
      flag = not flag
    answer = min(answer,temp,64-temp)
print(answer)
