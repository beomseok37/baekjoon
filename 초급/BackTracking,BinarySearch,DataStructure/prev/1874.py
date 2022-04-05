n = int(input())
arr = []
for i in range(n):
  arr.append(int(input()))

i = 0
stack = []
answer = []
for arr_i in range(n):
  if arr[arr_i]>i:
    stack += [i+j for j in range(1,arr[arr_i]-i+1)]
    answer += ['+']*(arr[arr_i]-i)
    i = arr[arr_i]
  elif arr[arr_i]<i:
    if stack[-1]!=arr[arr_i]:
      print('NO')
      exit()
  answer.append('-')
  stack.pop()

print('\n'.join(answer))
