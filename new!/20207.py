from functools import cmp_to_key
import sys
input = sys.stdin.readline

def compare(prev,curr):
    if prev[0]==curr[0]:
        return curr[1]-prev[1]
    else:
        return prev[0]-curr[0]

N = int(input())
s_e_list = []
result = 0
for _ in range(N):
    s_e_list.append(list(map(int,input().split())))
    
s_e_list.sort(key=cmp_to_key(compare))

temp = s_e_list[0:1]
start = temp[0][0]
end = temp[0][1]
for i in range(1,len(s_e_list)):
    s,e = s_e_list[i]
    
    if end + 1 < s:
        result += (end-start+1)*len(temp)
        start = s
        end = e
        temp = [[s,e]]
        continue
    
    for j in range(len(temp)):
        s_temp,e_temp = temp[j]
        if e_temp<s:
            temp[j]=[s,e]
            end = max(end,e)
            break
    else:
        end = max(end,e)
        temp.append([s,e])

result+= (end-start+1)*len(temp)
print(result)
