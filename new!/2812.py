from heapq import heapify
N, K = list(map(int, input().split()))
arr = list(input())
answer = ''

count = 0
s, e = 0, N
while count < K:
    temp = [[-int(item), s+idx] for idx, item in enumerate(arr[s:e])]
    heapify(temp)

    if temp[0][1]-s > K-count:
        print(1)
        answer = str(-temp[0][0])+answer
        count += e-temp[0][1]
        e = temp[0][1]
    elif temp[0][1]-s < K-count:
        print(2)
        answer = str(-temp[0][0])+answer
        count += temp[0][1]-s
        s = temp[0][1]+1
    else:
        print(3)
        answer = str(-temp[0][0])+answer
        count += temp[0][1]-s
    print(answer, count)
