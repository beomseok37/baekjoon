from itertools import combinations_with_replacement

n=int(input())
number=set()
roma=[1,5,10,50]

for bundle in combinations_with_replacement([0,1,2,3],n):
  total=0
  for i in bundle:
    total+=roma[i]
  number.add(total)
print(len(number))
