N, M = list(map(int, input().split()))
board = [list(input()) for _ in range(N)]
visited = [[-1 for _ in range(M)] for __ in range(N)]
moves = {'D': (1, 0), 'U': (-1, 0), 'L': (0, -1), 'R': (0, 1)}

count = 0
answer = 0
for i in range(N):
    for j in range(M):
        if visited[i][j] != -1:
            continue

        visited[i][j] = count
        stack = [(i, j)]
        while stack:
            r, c = stack.pop()

            nr, nc = r+moves[board[r][c]][0], c+moves[board[r][c]][1]

            if visited[nr][nc] == -1:
                stack.append((nr, nc))
                visited[nr][nc] = count
            elif visited[nr][nc] == count:
                answer += 1
                break
            else:
                break
        count += 1

print(answer)
