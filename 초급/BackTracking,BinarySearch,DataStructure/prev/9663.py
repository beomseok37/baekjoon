def backtracking(count):
  global answer
  if count==n:
    answer += 1
    return
  
  for i in range(n):
    queen[count] = i
    for j in range(count):
      if i == queen[j] or abs(i-queen[j])==abs(count-j):
        break
    else:
      backtracking(count+1)

answer = 0
n = int(input())
queen = [0]*15
  
backtracking(0)
print(answer)
