def fibo(n):
  if n == 0:
    return [1,0]
  if n == 1:
    return [0,1]
  if n in memo.keys():
    return memo[n]
  first, second = fibo(n-1), fibo(n-2)
  memo[n] = [first[0]+second[0],first[1]+second[1]]
  return memo[n]

count = int(input())
testCases = []
memo={}
for i in range(count):
  testCases.append(int(input()))

for testCase in testCases:
  zero, one = fibo(testCase)
  print(zero,one)
