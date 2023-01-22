import sys
input = sys.stdin.readline

def find_palindrome(num):
    if dp[num]!=-1:
        return dp[num]
    
    result = 0
    for middle in range(num+1):
        double_half = num-middle
        if double_half%2==0:
            result += find_palindrome(double_half//2)
    dp[num] = result
    return result

T = int(input())
test_case_list =[]
max_value = 0
for _ in range(T):
    new_value = int(input())
    test_case_list.append(new_value)
    max_value = max(max_value,new_value)

dp = [-1 for _ in range(max_value+1)]
dp[0]=1
dp[1]=1

for test_case in test_case_list:
    print(find_palindrome(test_case))
    
