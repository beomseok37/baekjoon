import sys
input = sys.stdin.readline

n,m = list(map(int,input().split()))
group = {}
belong = {}
for i in range(n):
  name = input().rstrip()
  count = int(input().rstrip())
  group[name] = []
  for j in range(count):
    person = input().rstrip()
    group[name].append(person)
    belong[person] = name
  group[name].sort()

for i in range(m):
  name = input().rstrip()
  test = int(input().rstrip())
  if test:
    print(belong[name])
  else:
    for person in group[name]:
      print(person)
