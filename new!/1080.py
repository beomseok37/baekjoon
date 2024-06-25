N, M = list(map(int, input().split()))
before = [list(map(int, list(input()))) for _ in range(N)]
after = [list(map(int, list(input()))) for _ in range(N)]
answer = 0
if (N < 3 or M < 3) and before != after:
    answer = -1
else:
    for i in range(N-2):
        for j in range(M-2):
            if before[i][j] != after[i][j]:
                answer += 1
                for k in range(3):
                    for l in range(3):
                        before[i+k][j+l] = 0 if before[i+k][j+l] == 1 else 1

if answer != -1 and before != after:
    print(-1)
else:
    print(answer)
