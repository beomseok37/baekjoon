n = int(input())
queue = [str(i) for i in range(1,n+1)]
answer = []
for i in range(n-1):
  answer.append(queue.pop(0))
  queue.append(queue.pop(0))
print(' '.join(answer+queue))
