from itertools import product
import sys
input = sys.stdin.readline

def make_even_palindrome(num):
    temp = []
    for nums in product([str(i) for i in range(10)],repeat=num//2):
        temp.append(''.join(nums+nums[::-1]))
    return temp

def make_odd_palindrome(num):
    temp = []
    for nums in product([str(i) for i in range(10)],repeat=num//2):
        for middle in range(10):
            temp.append(''.join(nums)+str(middle)+''.join(nums[::-1]))
    return temp

def make_palindrome(num):
    return make_even_palindrome(num) if num%2==0 else make_odd_palindrome(num)

N,M = list(map(int,input().split()))
result=0
remain1 = [[] for _ in range(M)]
remain2 = [[] for _ in range(M)]
for num in make_palindrome(N//2):
    temp1 = (int(num)*(10**(N//2)))%M
    temp2 = int(num)%M
    if str(num)[0]!='0':
        remain1[temp1].append(num)
    remain2[temp2].append(num)
for i in range(1,M):
    if remain1[i] and remain2[-i]:
        result += len(remain1[i])*len(remain2[-i])
result += len(remain1[0])*len(remain2[0])
print(result)
