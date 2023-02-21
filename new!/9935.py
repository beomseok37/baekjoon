import sys
input = sys.stdin.readline

string = input()[:-1]
bomb = input()[:-1]
stack = []
bomb_length = len(bomb)
last_bomb = bomb[-1]

for i in range(len(string)):
    stack.append(string[i])
    
    if last_bomb==stack[-1] and ''.join(stack[-bomb_length:]) == bomb:
        for _ in range(bomb_length):
            stack.pop()
        
print(''.join(stack) if stack else 'FRULA')
