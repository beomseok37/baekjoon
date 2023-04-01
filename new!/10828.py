import sys
input = sys.stdin.readline

N=int(input())
order_list=[input() for _ in range(N)]
stack=[]

for order in order_list:
    first_two_letter=order[0]+order[1]
    if first_two_letter=='pu':
        stack.append(int(order.split()[1]))
    elif first_two_letter=='po':
        print(-1 if not stack else stack.pop())
    elif first_two_letter=='si':
        print(len(stack))
    elif first_two_letter=='em':
        print(0 if stack else 1)
    else:
        print(-1 if not stack else stack[-1])
