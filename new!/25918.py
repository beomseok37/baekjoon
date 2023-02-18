import sys
input = sys.stdin.readline

N = int(input())
S = input()
stack = []
result = 0

for i in range(N):
    if not stack:
        stack.append([len(stack)+1,S[i]])
        continue
    
    if stack[-1][1] == S[i]:
        stack.append([len(stack)+1,S[i]])
    else:
        temp = stack.pop()
        result=max(result,temp[0])

if stack:
    print(-1)
else:
    print(result)
