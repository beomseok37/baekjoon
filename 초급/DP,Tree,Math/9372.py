import sys
input = sys.stdin.readline

def solution(nowCountry,planeCount):
  visited[nowCountry] = True
  for country in plane[nowCountry]:
    if not visited[country]:
      planeCount = solution(country,planeCount+1)
  return planeCount

caseCount = int(input())
for c in range(caseCount):
  countryNumber, planeNumber = list(map(int,input().split()))
  plane={}
  for i in range(1,countryNumber+1):
    plane[i] = set()
  for i in range(planeNumber):
    country1,country2 = list(map(int,input().split()))
    plane[country1].add(country2)
    plane[country2].add(country1)
  visited = [True] + [False]*(countryNumber)

  print(solution(1,0))
