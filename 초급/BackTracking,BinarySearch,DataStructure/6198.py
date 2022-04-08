n = int(input())
number = []
answer = 0

for i in range(n):
  number.append(int(input()))

stack = [0]
for i in range(1,n):
  while stack and number[stack[-1]]<=number[i]:
    answer += i-stack.pop()-1
  stack.append(i)
while stack:
  answer += n-stack.pop()-1

print(answer)
