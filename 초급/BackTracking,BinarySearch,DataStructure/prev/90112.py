n = int(input())
brackets=[]
for i in range(n):
  brackets.append(list(input()))

for bracketList in brackets:
  stack=[]
  flag = False
  for bracket in bracketList:
    if bracket=='(':
      stack.append(bracket)
    else:
      if stack:
        stack.pop()
      else:
        flag=True
        break
  if flag or stack:
    print("NO")
  else:
    print("YES")
