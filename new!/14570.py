import sys
input = sys.stdin.readline

n = int(input())
child_node = [[] for i in range(n+1)]

for i in range(1,n+1):
    u,v = list(map(int,input().split()))
    child_node[i].append(u)
    child_node[i].append(v)
k=int(input())

stack = [1]
while stack:
    node = stack.pop()
    left_child = child_node[node][0]
    right_child = child_node[node][1]
    if left_child==-1 and right_child==-1:
        break
    elif left_child!=-1 and right_child!=-1:
        if k % 2==1:
            k=k//2 +1
            stack.append(left_child)
        else:
            k=k//2
            stack.append(right_child)
    elif left_child!=-1:
        stack.append(left_child)
    else:
        stack.append(right_child)
    
print(node)
