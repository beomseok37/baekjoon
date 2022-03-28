import sys
read = sys.stdin.readline

n = int(read())
nodes = [0]*(n+1)
lines = []

for i in range(1,n+1):
  nodes[i] = set()
for i in range(n-1):
  node1, node2 = list(map(int,read().split()))
  lines.append([node1,node2])
  nodes[node1].add(node2)
  nodes[node2].add(node1)

D = 0
G = 0

for line in lines:
  node1, node2 = line
  D += (len(nodes[node1])-1)*(len(nodes[node2])-1)

for index in range(1,n+1):
  lineCount = len(nodes[index])
  if lineCount >=3:
    temp = lineCount*(lineCount-1)*(lineCount-2)
    G += temp//6
if D > G*3:
  print("D")
elif D < G*3:
  print("G")
else:
  print("DUDUDUNGA")


# import sys
# read = sys.stdin.readline


# n = int(read())
# nodes = {}
# visited = [0]*(n+1)

# for i in range(1,n+1):
#   nodes[i] = set()
# for i in range(n-1):
#   number1, number2 = list(map(int,read().split()))
#   nodes[number1].add(number2)
#   nodes[number2].add(number1)

# D = 0
# G = 0

# stack = [1]
# visited[1] = 1
# count = 1

# while stack:
#   stackNode = stack.pop(0)
#   degree = len(nodes[stackNode])
#   if degree >= 3:
#     G += (degree*(degree-1)*(degree-2))//6

#   stack2 = [[stackNode,1]]
#   visited2 = [stackNode]
#   while stack2:
#     stack2Node,count = stack2.pop()
#     if count == 4:
#       D+=1
#       continue
#     for canVisitNode in nodes[stack2Node]:
#       if canVisitNode not in visited2 and not visited[canVisitNode]:
#         visited2.append(canVisitNode)
#         stack2.append([canVisitNode,count+1])
  
#   for canVisitNode in nodes[stackNode]:
#     if not visited[canVisitNode]:
#       visited[canVisitNode] = 1
#       stack.append(canVisitNode)

#   count += 1
      
# if D > G*3:
#   print("D")
# elif D < G*3:
#   print("G")
# else:
#   print("DUDUDUNGA")
