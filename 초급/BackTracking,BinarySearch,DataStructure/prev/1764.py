n,m = list(map(int,input().split()))
listen = set()
watch = set()

for i in range(n):
  listen.add(input())
for j in range(m):
  watch.add(input())

answer = sorted(list(listen&watch))

print(len(answer))
for person in answer:
  print(person)
