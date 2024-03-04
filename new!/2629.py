# N = int(input())
# weights = list(map(int, input().split()))
# M = int(input())
# checks = list(map(int, input().split()))
# weightSum = sum(weights)
# dp = [-1 for _ in range(weightSum+1)]
# visited = [False for _ in range(N)]
# answer = [0 for _ in range(M)]

# dp[0] = 1


# def recursion(i, num, checkI):
#     dp[num]=1

#     for j in range(i, N):
#         if visited[j]:
#             continue

#         visited[j] = True
#         flag = recursion(i+1, num+weights[j], checkI)
#         visited[j] = False

#     return flag


# def oppositeRecursion(num):
#     if num < 0:
#         return
#     if dp[num] != -1:
#         return dp[num]

#     flag = 0
#     for i in range(N):
#         if not visited[i]:
#             continue

#         visited[i] = True
#         flag = oppositeRecursion(num-weights[i])
#         visited[i] = False

#         if flag == 1:
#             dp[num] = 1
#             return flag
#     dp[num] = 0
#     return flag


# for i in range(M):
#     recursion(0, 0, i)


# str = ''
# for checkI in range(M):
#     if answer[checkI] == 1 or dp[checks[checkI]] == 1:
#         str += 'Y'
#     else:
#         str += 'N'
#     str += ' ' if checkI < M-1 else ''
# print(str)


N = int(input())
weights = list(map(int, input().split()))
M = int(input())
checks = list(map(int, input().split()))
weightSum = sum(weights)
dp = [-1 for _ in range(weightSum+1)]
visited = [False for _ in range(N)]
temp = [0 for _ in range(M)]

dp[0] = 1


def recursion(num, checkI):
    if num < 0:
        return 0
    if dp[num] != -1:
        return dp[num]
    flag = oppositeRecursion(num-checks[checkI])
    if flag > 0:
        temp[checkI] = 1

    for i in range(N):
        if visited[i]:
            continue
        visited[i] = True
        flag += recursion(num-weights[i], checkI)
        visited[i] = False

    dp[num] = flag
    return flag


def oppositeRecursion(num):
    if num < 0:
        return 0
    if dp[num] != -1:
        return dp[num]
    flag = 0
    for i in range(N):
        if not visited[i]:
            continue

        visited[i] = False
        flag += oppositeRecursion(num-weights[i])
        visited[i] = True

    dp[num] = flag
    return flag


for i in range(M):
    recursion(weightSum, i)

str = ''
for checkI in range(M):
    if temp[checkI] == 1 or dp[checks[checkI]] > 1:
        str += 'Y'
    else:
        str += 'N'
    str += ' ' if checkI < M-1 else ''
print(dp)
print(temp)
print(str)
