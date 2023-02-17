import sys
input = sys.stdin.readline

def recursion(now_room,now_money):
    global flag,length
    if flag:
        return
    
    if miro[now_room][0] == 'L':
        now_money = max(now_money,int(miro[now_room][1]))
    elif miro[now_room][0] == 'T': # 트롤
        if int(miro[now_room][1]) > now_money:
            return;
        else:
            now_money -= int(miro[now_room][1])

    if now_room == length-1:
        flag=True
        return;
    
    visited[now_room] = True
    for next_room in miro[now_room][2:]:
        if not visited[int(next_room)-1]:
            recursion(int(next_room)-1,now_money)
    visited[now_room] = False

n = int(input())
miro_list=[]
while n!=0:
    temp=[input().split()[:-1] for _ in range(n)]
    miro_list.append(temp)
    n = int(input())
    
for miro in miro_list:
    flag = False
    length = len(miro)
    visited = [False for _ in range(length)]
    
    recursion(0,0)
    print('Yes' if flag else 'No')
