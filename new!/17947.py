import sys;
input = sys.stdin.readline
N, M, K = map(int, input().split())
flower_war = set([i for i in range(1,4*N+1)])

for _ in range(M+1):
    a, b = map(int, input().split())
    flower_war.remove(a)
    flower_war.remove(b)
flower_war = list(flower_war)

for i in range(len(flower_war)):
    flower_war[i] %= K
flower_war.sort()

score = abs(a % K - b % K)

s,e = 0, len(flower_war) // 2
result = 0
while e < len(flower_war) and result < M - 1:
    if flower_war[e] - flower_war[s] > score:
        result, s, e = result + 1, s + 1, e + 1
    else:
        e += 1

print(result)
