N = int(input())
M = int(input())
length = len(str(N))
brokenList = [False for _ in range(10)]

if M != 0:
    for broken in list(map(int, input().split())):
        brokenList[broken] = True

if N == 100:
    print(0)
    exit()


def dfs(i, cur):
    global answer
    if i != 0 and length - 1 <= i <= length+1:
        answer = min(answer, abs(N-cur)+len(str(cur)))
    if i == length+1:
        return

    for k in range(10):
        if brokenList[k]:
            continue
        dfs(i+1, cur*10+k)


answer = abs(100-N)
dfs(0, 0)
print(answer)
