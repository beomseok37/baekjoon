from queue import PriorityQueue
from collections import defaultdict

N, K = list(map(int, input().split()))
things = list(map(int, input().split()))

if N >= K:
    print(0)
    exit()

multitab = set()
answer = 0

for i, thing in enumerate(things):
    multitab.add(thing)
    if len(multitab) <= N:
        continue

    answer += 1

    later_used = 0
    later_idx = -1
    for plug in multitab:
        try:
            index = things[i:].index(plug)
        except:
            index = K

        if later_idx < index:
            later_used = plug
            later_idx = index

    multitab.discard(later_used)

print(answer)
