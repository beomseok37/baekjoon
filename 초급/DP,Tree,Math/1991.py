n = int(input())
tree = {}
for i in range(n):
  node,first,second = input().split()
  tree[node] = [first,second]

def preOrder(nowNode):
  if nowNode == '.':return
  firstChild, secondChild = tree[nowNode]
  print(nowNode,end='')
  preOrder(firstChild)
  preOrder(secondChild)

def inOrder(nowNode):
  if nowNode == '.':return
  firstChild, secondChild = tree[nowNode]
  inOrder(firstChild)
  print(nowNode,end='')
  inOrder(secondChild)

def postOrder(nowNode):
  if nowNode == '.':return
  firstChild, secondChild = tree[nowNode]
  postOrder(firstChild)
  postOrder(secondChild)
  print(nowNode,end='')

preOrder('A')
print()
inOrder('A')
print()
postOrder('A')
print()
