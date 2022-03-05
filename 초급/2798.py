from itertools import combinations

number, target = list(map(int,input().split(' ')))
arr = list(map(int,input().split()))
closestSum = 0
for threeNumbers in combinations(arr,3):
  if target>=sum(threeNumbers) and closestSum < sum(threeNumbers):
    closestSum = sum(threeNumbers)
print(closestSum)
