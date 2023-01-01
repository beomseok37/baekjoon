import sys
input = sys.stdin.readline

def find(class_room):
    if class_room == parent[class_room]:
        return class_room
    parent[class_room] = find(parent[class_room])
    return parent[class_room]

def union(a,b):
    a_parent = find(a)
    b_parent = find(b)
    if a_parent != b_parent:
        parent[a_parent] = b_parent

n,m = list(map(int,input().split()))
parent = [i for i in range(n+1)]
result=0

for i in range(m):
    a,b = list(map(int,input().split()))
    union(a,b)
    
lecture_list = list(map(int,input().split()))
for i in range(n-1):
    prev_class,after_class = lecture_list[i],lecture_list[i+1]
    
    if find(prev_class) != find(after_class):
        result+=1
print(result)
