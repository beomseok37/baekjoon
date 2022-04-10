def fibo(n):
  if n == 1:
    return [1,0]
  if n == 2:
    return [0,1]
  if n in memo.keys():
    return memo[n]
  first, second = fibo(n-1), fibo(n-2)
  memo[n] = [first[0]+second[0],first[1]+second[1]]
  return memo[n]

day, riceCake = list(map(int,input().split()))
memo = {}
a,b = fibo(day)
for i in range(riceCake//b,0,-1):
  temp = riceCake - i*b
  firstRiceCake = temp/a
  if firstRiceCake!=0 and firstRiceCake == int(firstRiceCake):
    print(int(firstRiceCake))
    print(i)
    break
