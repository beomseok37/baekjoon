N = int(input())
heights = list(map(int, input().split()))
answer = [0 for _ in range(N)]
stack = [(heights.pop(), N-1)]
for i in range(N-1):
    height = heights.pop()
    while stack and stack[-1][0] < height:
        h, index = stack.pop()
        answer[index] = N-1-i
    stack.append((height, N-2-i))
print(' '.join(map(str, answer)))
