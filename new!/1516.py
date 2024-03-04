def recursion(num):
    if dp[num] != 0:
        return dp[num]

    temp = 0
    for i in range(1, len(components[num])):
        temp = max(temp, recursion(components[num][i]-1))
    dp[num] = temp+components[num][0]
    return dp[num]


N = int(input())
components = [list(map(int, input().split()[:-1])) for _ in range(N)]
dp = [0 for _ in range(N)]

for i in range(N):
    if len(components[i]) == 1:
        dp[i] = components[i][0]

for i in range(N):
    print(recursion(i))
