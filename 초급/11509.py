N = int(input())
heights = list(map(int,input().split()))
arrows = [0] * 1000001
answer = 0

for i in range(N):
  if arrows[heights[i]]==0:
    answer+=1
    arrows[heights[i]-1]+=1
  else:
    arrows[heights[i]]-=1
    arrows[heights[i]-1]+=1
print(answer)
