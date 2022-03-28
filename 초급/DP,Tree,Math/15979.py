m,n = list(map(abs,map(int, input().split())))
if m == 0 and n == 0:
  print(0)
  exit()
while n:
  m ,n = n, m % n
print(m if m == 1 else 2)
