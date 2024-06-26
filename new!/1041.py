import sys
input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))
if N == 1:
    nums.sort()
    print(sum(nums[:5]))
else:
    answer = 0
    sumLists = []
    sumLists.append(min(nums[0], nums[5]))
    sumLists.append(min(nums[1], nums[4]))
    sumLists.append(min(nums[2], nums[3]))
    sumLists.sort()

    min1 = sumLists[0]
    min2 = sumLists[0] + sumLists[1]
    min3 = sumLists[0] + sumLists[1] + sumLists[2]

    n1 = 5*N*N - 16*N + 12
    n2 = 8*N-12
    n3 = 4

    answer += n1 * min1
    answer += n2 * min2
    answer += n3 * min3

    print(answer)
