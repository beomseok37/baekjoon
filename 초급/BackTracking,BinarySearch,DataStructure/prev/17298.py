n = int(input())
numbers = list(map(int,input().split()))
answers = [-1]*n
stack = [0]

for i in range(1,n):
  while stack and numbers[stack[-1]]<numbers[i]:
    number = stack.pop()
    answers[number]=numbers[i]
  stack.append(i)
print(' '.join(map(str,answers)))
