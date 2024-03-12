N, S = list(map(int, input().split()))
arr = list(map(int, input().split()))
prefix = [0]
for i in range(N):
    prefix.append(prefix[-1]+arr[i])

answer = 100_001
s, e = 0, 0
while e <= N:
    if prefix[e]-prefix[s] < S:
        e += 1
        continue

    answer = min(answer, e-s)
    s += 1

print(answer if answer != 100_001 else 0)
