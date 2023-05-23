N = int(input())
A = list(map(int, input().split()))
rA = A[::-1]
increase,decrease = [1 for _ in range(N)],[1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            increase[i] = max(increase[i], increase[j]+1)
        if rA[i] > rA[j]:
            decrease[i] = max(decrease[i], decrease[j]+1)

answer=0
for i in range(N):
    answer = max(answer,increase[i] + decrease[N-1-i] - 1)

print(answer)
