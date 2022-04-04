import sys
input = sys.stdin.readline

def push(number):
  if len(pq) == 1:
    pq.append(number)
    return
  pq.append(number)
  child = len(pq)-1
  parent = child//2
  while parent and pq[child]<pq[parent]:
    pq[child],pq[parent] = pq[parent],pq[child]
    child = parent
    parent = child//2

def findSmallerChild(now):
  if now*2>len(pq)-1:
    return 0
  elif now*2 == len(pq)-1:
    return now*2
  else:
    if pq[now*2]<pq[now*2+1]:
      return now*2
    else:
      return now*2+1

def pop():
  if len(pq) == 1:
    return 0
  if len(pq) == 2:
    return pq.pop()  
  value = pq[1]
  pq[1] = pq.pop()
  parent = 1
  smallerChild = findSmallerChild(parent)
  while smallerChild and pq[parent] > pq[smallerChild]:
    pq[parent], pq[smallerChild] =pq[smallerChild], pq[parent]
    parent = smallerChild
    smallerChild = findSmallerChild(parent)

  return value


n = int(input().rstrip())
pq = [0]
arr = []
for i in range(n):
  arr.append(int(input().rstrip()))

for number in arr:
  if number == 0:
    print(pop())
  else:
    push(number)
