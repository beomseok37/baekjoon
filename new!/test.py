from collections import deque
alp,cop=10,10
problems=[[10,15,2,1,2],[20,20,3,3,4]]
answer = 10000000000
queue=deque()
queue.append([alp,cop,0])
while queue:
    print(queue)
    curAlp,curCop,cost=queue.popleft()
    
    flag1,flag2=True,True
    for problem in problems:
        if curAlp>=problem[0] and curCop>=problem[1]:
            flag1=False
        else:
            flag2=False
    
    if flag1:
        queue.append([curAlp+1,curCop,cost+1])
        queue.append([curAlp,curCop+1,cost+1])
        continue
        
    if flag2:
        answer=min(answer,cost)
        continue
    
    for problem in problems:
        if curAlp>=problem[0] and curCop>=problem[1]:
            queue.append([curAlp+problem[2],curCop+problem[3],cost+problem[4]])
