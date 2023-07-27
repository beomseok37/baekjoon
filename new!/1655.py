import sys
from queue import PriorityQueue
input = sys.stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]

leftQueue = PriorityQueue()
rightQueue = PriorityQueue()
middle = nums[0]
print(middle)

for i in range(1,N):
    now = nums[i]
    
    if i%2==1:
        if now<=middle:
            leftQueue.put((-now,now))
            rightQueue.put(middle)
            middle = leftQueue.get()[1]
        else:
            rightQueue.put(now)
    else:
        if now<=middle:
            leftQueue.put((-now,now))
        else:
            rightQueue.put(now)
            leftQueue.put((-middle,middle))
            middle = rightQueue.get()
    
    print(middle)
