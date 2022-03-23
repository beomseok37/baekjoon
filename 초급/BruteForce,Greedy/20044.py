number = int(input())
powers = list(map(int,input().split()))
powers.sort()
answer = 200000
while powers:
  answer = min(answer,powers[0]+powers[-1])
  powers = powers[1:-1]
print(answer)
