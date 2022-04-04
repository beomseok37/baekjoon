import sys
input = sys.stdin.readline

n,m = list(map(int,input().split()))
pocketmons=[]
pocketmonDict={}

for i in range(n):
  pocketmon = input().rstrip()
  pocketmons.append(pocketmon)
  pocketmonDict[pocketmon] = i+1

for i in range(m):
  test = input().rstrip()
  if test.isdigit():
    print(pocketmons[int(test)-1])
  else:
    print(pocketmonDict[test])
