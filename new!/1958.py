str1 = list(input())
str2 = list(input())
str3 = list(input())

dp = [[[0 for _ in range(len(str3)+1)] for __ in range(len(str2)+1)]
      for ___ in range(len(str1) + 1)]
answer = 0
for i in range(1, len(str1)+1):
    for j in range(1, len(str2)+1):
        for k in range(1, len(str3)+1):
            if str1[i-1] == str2[j-1] == str3[k-1]:
                dp[i][j][k] = dp[i-1][j-1][k-1] + 1
            else:
                dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])

            answer = max(answer, dp[i][j][k])
print(answer)
