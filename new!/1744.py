N = int(input())
arr = [int(input()) for _ in range(N)]
flag = True
plus, minus = [], []

if len(arr) == 1:
    print(arr[0])
    exit()

for num in arr:
    if num > 0:
        plus.append(num)
    elif num < 0:
        minus.append(num)
    else:
        flag = False

answer = 0
plus.sort(reverse=True)
minus.sort()

for i in range(0, len(plus)-1, 2):
    if plus[i] != 1 and plus[i+1] != 1:
        answer += plus[i]*plus[i+1]
    else:
        answer += plus[i]+plus[i+1]
for i in range(0, len(minus)-1, 2):
    answer += minus[i]*minus[i+1]

if len(plus) % 2 == 1:
    answer += plus[-1]
if len(minus) % 2 == 1 and flag:
    answer += minus[-1]
print(answer)
