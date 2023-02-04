import sys
input = sys.stdin.readline

N,K = list(map(int,input().split()))
room_info_list = [[] for _ in range(N)]
dp = [[[0,0,0] for __ in range(201)] for _ in range(200)]

for i in range(N):
    left_room,right_room = list(map(int,input().split()))
    room_info_list[i].append(left_room)
    room_info_list[i].append(right_room)
input()

dp[0][1][0] = room_info_list[0][1]
dp[0][1][1] = room_info_list[0][0]
dp[0][0][2] = room_info_list[0][0]+room_info_list[0][1]

for i in range(1,N):
    for j in range(K+1):
        if j>=1:
            dp[i][j][0] = max(dp[i-1][j-1][0],dp[i-1][j-1][2]) + room_info_list[i][1]
            dp[i][j][1] = max(dp[i-1][j-1][1],dp[i-1][j-1][2]) + room_info_list[i][0]
        if i+1!=j:
            dp[i][j][2] = max(max(dp[i-1][j][0],dp[i-1][j][1]),dp[i-1][j][2])+room_info_list[i][0]+room_info_list[i][1]
print(max(max(dp[N-1][K][0],dp[N-1][K][1]),dp[N-1][K][2]))
