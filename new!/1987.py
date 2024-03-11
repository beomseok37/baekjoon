R, C = list(map(int, input().split()))
board = [list(input()) for _ in range(R)]
moves = [(-1, 0), (1, 0), (0, 1), (0, -1)]

visited = [False for _ in range(26)]


def dfs(r, c, count):
    answer = count
    for i in range(4):
        nr, nc = r+moves[i][0], c+moves[i][1]

        if not (0 <= nr < R and 0 <= nc < C):
            continue

        num = ord(board[nr][nc])-ord('A')

        if visited[num]:
            continue

        visited[num] = True
        answer = max(answer, dfs(nr, nc, count+1))
        visited[num] = False

    return answer


visited[ord(board[0][0])-ord('A')] = True
print(dfs(0, 0, 1))
