N = int(input())
slime = list(map(int,input().split()))
slime.sort()
answer = 0

while len(slime)!=1:
  newSlime = slime[0]+slime[1]
  answer += slime[0]*slime[1]
  slime = slime[2:]
  first = 0
  last = len(slime)-1
  while first<last:
    temp = (first+last)//2
    if slime[temp]>newSlime:
      last = temp-1
    elif slime[temp]<=newSlime:
      first = temp+1
  slime.insert(first,newSlime)
print(answer)
