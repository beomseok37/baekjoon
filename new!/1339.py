N = int(input())

alpha = [input() for _ in range(N)] 
alpha_dict = {} 

for i in range(N): 
    for j,a in enumerate(alpha[i]): 
        if a in alpha_dict: 
            alpha_dict[a] += 10 ** (len(alpha[i])-j-1) 
        else:   
            alpha_dict[a] = 10 ** (len(alpha[i])-j-1)

numList = sorted(alpha_dict.values(),reverse=True)
total = 0
n = 9
for num in numList: 
    total += n * num
    n -= 1

print(total)
