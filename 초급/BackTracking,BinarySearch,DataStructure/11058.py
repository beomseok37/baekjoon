#아직 해결 못함

def bt(n,k,a,b):
  global answer
  if n==k:
    answer=max(answer,a)
    return
  if n>=k+3 and (n-k)*b<a*(n-k-2):
    bt(n,k+3,a*2,a)
  if b>1:
    bt(n,k+1,a+b,b)

n = int(input())
answer = 0
if n<=6:
  print(n)
else:
  for i in range(3,n):
    bt(n,i,i,0)
  print(answer)
