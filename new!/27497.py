import sys
input = sys.stdin.readline

N = int(input())
temp_list=[]
front, back = [], []
flag_list = []

for j in range(N):
    temp = input()
    if temp[0]=='1':
        flag_list.append(1)
        back.append(temp[2])
    elif temp[0]=='2':
        flag_list.append(-1)
        front.append(temp[2])
    else:
        if flag_list:
            flag = flag_list.pop()
            if flag>0:
                back.pop()
            else:
                front.pop()

result=''.join(reversed(front))+''.join(back)

print(result if flag_list else 0)
