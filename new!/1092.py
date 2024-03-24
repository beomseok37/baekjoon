N = int(input())
cranes = list(map(int, input().split()))
M = int(input())
boxes = list(map(int, input().split()))
cranes.sort(reverse=True)
boxes.sort(reverse=True)

if boxes[0] > cranes[0]:
    print(-1)
else:
    result = 0
    while boxes:
        for crane in cranes:
            if boxes and crane < boxes[-1]:
                continue
            for box in boxes:
                if crane >= box:
                    boxes.remove(box)
                    break
        result += 1
    print(result)
