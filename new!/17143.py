# def move(r,c,s,d):
#     global R,C
#     tr,tc,ts,td=r,c,s,d
#     if d<=2:
#         if d==1 and ts>=tr-1:
#             ts-=tr-1
#             tr=1
#             td=2
#         elif d==2 and ts>=R-tr:
#             ts-=R-tr
#             tr=R
#             td=1
        
#         while ts>=R-1:
#             ts-=R-1
#             tr=R if tr==1 else 1
#             td=1 if td==2 else 2
        
#         if ts>0:
#             if td==1:
#                 tr-=ts
#             else:
#                 tr+=ts
#     else: # 좌우
#         if d==3 and ts>=C-tc:
#             ts-=C-tc
#             tc=C
#             td=4
#         elif d==4 and ts>=tc-1:
#             ts-=tc-1
#             tc=1
#             td=3
#         while ts>=C-1:
#             ts-=C-1
#             tc=C if tc==1 else 1
#             td=4 if td==3 else 3
#         if ts>0:
#             if td==4:
#                 tc-=ts
#             else:
#                 tc+=ts
#     return [tr,tc,td]

# R,C,M=list(map(int,input().split()))
# # 0:행 1:열 2:속력 3:이동방향 4:사이즈
# # 1:위 2: 아래 3:오른쪽 4:왼쪽
# sharks=[]
# sea=[-1 for _ in range(C+1)]
# catches=0
# for i in range(M):
#     temp=list(map(int,input().split()))
#     temp.append(0)
#     sharks.append(temp)

# for i,shark in enumerate(sharks):
#     if sea[shark[1]]==-1:
#         sea[shark[1]]=i
#     else:
#         if shark[0] < sharks[sea[shark[1]]][0]:
#             sea[shark[1]]=i

# for i in range(1,C+1):
#     if sea[i]!=-1:
#         catches+=sharks[sea[i]][4]
#         sharks[sea[i]][5]=1
    
#     sea=[-1 for _ in range(C+1)]
#     board=[[0 for _ in range(C+1)] for __ in range(R+1)]
#     for i in range(M):
#         if sharks[i][5]==1:
#             continue
        
#         [tr,tc,td] = move(sharks[i][0],sharks[i][1],sharks[i][2],sharks[i][3])
#         sharks[i][0],sharks[i][1],sharks[i][3]=tr,tc,td
#         if board[tr][tc]==0:
#             board[tr][tc]=i
#         else:
#             if sharks[i][4]>sharks[board[tr][tc]][4]:
#                 board[tr][tc]=i
#                 sharks[board[tr][tc]][5]=1
#             else:
#                 sharks[i][5]=1
    
#     for i in range(M):
#         if sharks[i][5]==1:
#             continue
#         if sea[sharks[i][1]]==-1:
#             sea[sharks[i][1]]=i
#         else:
#             if sharks[i][0] < sharks[sea[sharks[i][1]]][0]:
#                 sea[sharks[i][1]]=i
# print(catches)

import sys; input = sys.stdin.readline

# 상어 이동 함수
def move_shark():
    g = [[[] for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if graph[i][j]:
                x, y = i, j
                s, d, z = graph[i][j][0]
                dist = s
                # 상어의 속도만큼 1칸씩 이동
                while 0 < dist:
                    nx = x + direction[d][0]
                    ny = y + direction[d][1]
                    # 맵 내부에서 이동하는 경우
                    if 0 <= nx < R and 0 <= ny < C:
                        x, y = nx, ny
                        dist -= 1 # 이동해야 할 남은 거리 1 차감
                    # 벽과 충돌하는 경우, 현재 진행방향별 방향전환
                    else:
                        # d(0-1-2-3) : 방향(상-하-우-좌)
                        # 상 to 하 or 우 to 좌
                        if d == 0 or d == 2:
                            d += 1
                        # 하 to 상 or 좌 to 우
                        elif d == 1 or d == 3:
                            d -= 1
                        continue
                g[x][y].append([s, d, z])

    for i in range(R):
        for j in range(C):
            graph[i][j] = g[i][j]

# 상어 낚시 함수
def catch_shark():
    global answer
    # 낚시왕이 칼럼 방향으로 이동하며 낚시를 하기 때문에 칼럼 우선순위
    for i in range(C):
        for j in range(R):
            # 상어가 존재하는 경우
            if graph[j][i]:
                answer += graph[j][i][0][2]
                graph[j][i].remove(graph[j][i][0])
                break

        move_shark()
        for m in range(R):
            for n in range(C):
                # 한 좌표에 상어가 2마리 이상 있는 경우
                if 1 < len(graph[m][n]):
                    # 몸집이 작은 순서대로 상어 제거
                    graph[m][n].sort(key=lambda x: x[2], reverse=True)
                    while 1 < len(graph[m][n]):
                        graph[m][n].pop()

if __name__ == '__main__':
    R, C, M = map(int, input().split())
    # 진행방향: 상, 하, 우, 좌
    direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    graph = [[[] for _ in range(C)] for _ in range(R)]
    for _ in range(M):
        r, c, s, d, z = map(int, input().split())
        graph[r-1][c-1].append([s, d-1, z])

    answer = 0
    catch_shark()
    print(answer)
