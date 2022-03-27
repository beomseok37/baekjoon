n = int(input())
rings = list(map(int,input().split()))

for i in range(1,len(rings)):
  firstRing = rings[0]
  ring = rings[i]
  while ring:
    firstRing, ring = ring, firstRing%ring
  print(str(rings[0]//firstRing)+'/'+str(rings[i]//firstRing))
