import sys
input = sys.stdin.readline

def GCD(x,y):
    while y:
        x,y=y,x%y
    return x

def LCM(x,y):
    return (x*y)//GCD(x,y)

n,s = list(map(int,input().split()))
m = int(input())
m_list = []
m_LCM = 0
m_LCM_sum = 0
removed_fried = n - s
remain = 0
result = -1

for i in range(m):
    m_list.append(int(input()))
    
m_LCM = LCM(m_list[0],m_list[1]) if m != 1 else m_list[0]
for i in range(2,m):
    m_LCM = LCM(m_LCM,m_list[i])

for i in range(m):
    m_LCM_sum += m_LCM//m_list[i]

if removed_fried > m_LCM_sum:
    remain = removed_fried % m_LCM_sum
    remain = remain if remain!=0 else m_LCM_sum
else:
    remain = removed_fried

count = 0
for i in range(m_LCM):
    for j in range(m):
        if i%m_list[j]==0:
            count+=1
        if count==remain:
            result=j
            break
    if result!=-1:
        break

print(result+1)
