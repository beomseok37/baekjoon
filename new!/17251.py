import sys
input = sys.stdin.readline

N = int(input())
power = list(map(int,input().split()))

max_power_index=[0]
for i in range(1,N):
    if power[max_power_index[0]]<power[i]:
        max_power_index=[i]
    elif power[max_power_index[0]]==power[i]:
        max_power_index.append(i)

blue=max_power_index[0]
red=N-max_power_index[-1]-1

if red==blue:
    print('X')
else:
    print('R' if red>blue else 'B')
