def dp(index):
  if memo[index] != 0:
    return memo[index]
  
  memo[index] = dp(index-1)+dp(index-2)
  return memo[index]

k = int(input())
memo = [0]*50
memo[1] = 1
memo[2] = 1

dp(k)

print(memo[k-1], memo[k])
