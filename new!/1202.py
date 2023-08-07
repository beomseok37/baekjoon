import heapq
    
N,K = list(map(int,input().split()))
gems = [list(map(int,input().split())) for _ in range(N)]
bags = [int(input()) for _ in range(K)]
sortedGems=[]
bags.sort()
gems.sort()
answer=0

for bag in bags:
    while gems and gems[0][0]<=bag:
        heapq.heappush(sortedGems,-gems[0][1])
        heapq.heappop(gems)
    if sortedGems:
        answer-=heapq.heappop(sortedGems)

print(answer)
