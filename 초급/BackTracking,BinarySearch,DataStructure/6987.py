from itertools import combinations

results = [[],[],[],[]]
for i in range(4):
  string = list(map(int,input().split()))
  for j in range(18):
    if j%3==0:
      results[i].append([string[j]])
    else:
      results[i][-1].append(string[j])
  results[i].sort(key=lambda x: x[0],reverse=True)
combination=[]
for pair in combinations([i for i in range(6)],2):
  combination.append(pair)

def check(i,now):
  newResult = now[:]
  if i==15:
    for j in range(6):
      for k in range(3):
        if newResult[j][k]:
          return 1
    return 0
  value=1
  isIt=True
  pair = combination[i]
  win1,tie1,lose1=newResult[pair[0]]
  win2,tie2,lose2=newResult[pair[1]]
  if win1 and lose2:
    newResult[pair[0]][0]-=1
    newResult[pair[1]][2]-=1
    value *= check(i+1,newResult)
    newResult[pair[0]][0]+=1
    newResult[pair[1]][2]+=1
    isIt=False
  if win2 and lose1:
    newResult[pair[1]][0]-=1
    newResult[pair[0]][2]-=1
    value *= check(i+1,newResult)
    newResult[pair[1]][0]+=1
    newResult[pair[0]][2]+=1
    isIt=False
  if tie1 and tie2:
    newResult[pair[1]][1]-=1
    newResult[pair[0]][1]-=1
    value *= check(i+1,newResult)
    isIt=False
  if isIt:
    for j in range(6):
      for k in range(3):
        if newResult[j][k]:
          return 1
    return 0
  return value

for result in results:
  print('1' if check(0,result)==0 else '0',end=" ")
print()
