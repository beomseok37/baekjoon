n,k = list(map(int,input().split()))

queue = [str(i) for i in range(1,n+1)]
answer = []
num = 0
for i in range(n):
    num += k-1  
    if num >= len(queue):
        num = num%len(queue)
 
    answer.append(str(queue.pop(num)))
print("<"+', '.join(answer)+">")
