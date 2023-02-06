import sys
input = sys.stdin.readline

def move(ball):
    last_ball = ball[0]
    connected_ball_count=1
    ball_count=1
    flag=True
    for i in range(1,N):
        if ball[i]==last_ball:
            if flag:
                connected_ball_count+=1
            ball_count+=1
        else:
            flag=False
    return ball_count-connected_ball_count if ball_count-connected_ball_count<N-ball_count else N-ball_count

N = int(input())
ball = list(input())[:-1]

print(min(move(ball),move(list(reversed(ball)))))
