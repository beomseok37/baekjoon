number, length = list(map(int,input().split(' ')))
fruits = list(map(int,input().split(' ')))
fruits.sort()
for fruit in fruits:
  length += 1 if length >= fruit else 0
print(length)
