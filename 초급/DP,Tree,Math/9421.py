n = int(input())
memo=[0]*(n+2)
for i in range(2,n+1):
  temp = i*2
  while temp<=n:
    memo[temp] += 1
    temp += i
  if memo[i] == 0:
    array = []
    nextRoot = i
    while True:
      tempString = str(nextRoot)
      nextRoot = 0
      for s in tempString:
        nextRoot += int(s)**2
      if nextRoot == 1:
        print(i)
        break
      if nextRoot in array:
        break
      array.append(nextRoot)
    