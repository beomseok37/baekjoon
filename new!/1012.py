import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
d = [(-1, 0), (0, -1), (0, 1), (1, 0)]


def dfs(r, c):
    global N, M
    for i in range(4):
        nr, nc = r+d[i][0], c+d[i][1]

        if not (0 <= nr < N and 0 <= nc < M) or ground[nr][nc] == 0 or visited[nr][nc]:
            continue

        visited[nr][nc] = True
        dfs(nr, nc)


for i in range(int(input())):
    M, N, K = list(map(int, input().split()))
    ground = [[0 for _ in range(M)] for __ in range(N)]
    visited = [[False for _ in range(M)] for __ in range(N)]
    count = 0

    for _ in range(K):
        c, r = list(map(int, input().split()))
        ground[r][c] = 1

    for i in range(N):
        for j in range(M):
            if visited[i][j] or ground[i][j] == 0:
                continue

            count += 1
            visited[i][j] = True
            dfs(i, j)

    print(count)
