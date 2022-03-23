num = int(input())
array = list(map(int,input().split(' ')))
total, share = 0, 0
for number in array:
  total += number
  share += number // 2
print('YES' if total % 3 == 0 and total//3<=share else 'NO')
