H,W = list(map(int,input().split(' ')))
number = int(input())
stickers = []
for i in range(number):
  stickers.append(sorted(list(map(int,input().split(' ')))))

answer = 0
x1=[0,0,1,1]
y1=[1,1,0,0]
x2=[0,1,0,1]
y2=[1,0,1,0]
for i in range(number-1):
  for j in range(i+1,number):
    for k in range(4):
      temp1 = stickers[i][x1[k]]+stickers[j][x2[k]]
      temp2 = max(stickers[i][y1[k]],stickers[j][y2[k]])
      if H >= temp1 and W >= temp2 or H >= temp2 and W >= temp1:
        answer = max(answer,stickers[i][x1[k]]*stickers[i][y1[k]]+stickers[j][x2[k]]*stickers[j][y2[k]])
print(answer)
