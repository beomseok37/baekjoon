from itertools import combinations
import sys
input = sys.stdin.readline

N,M = list(map(int,input().split()))

city = []
chicken = []
home=[]
result = 10000
for i in range(N):
    temp = list(map(int,input().split()))
    for j in range(N):
        if temp[j]==2:
            chicken.append([i,j])
        if temp[j]==1:
            home.append([i,j])
    city.append(temp)

for chicken_position in combinations(chicken,M):    
    each_result = 0
    for h_r,h_c in home:
        each_minimum = 101
        for r,c in chicken_position:
            each_minimum = min(each_minimum, abs(r-h_r)+abs(c-h_c))
        each_result +=each_minimum
    result = min(each_result,result)

print(result)
