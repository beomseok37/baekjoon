N = int(input())

alpha = [input() for _ in range(N)] 
alpha_dict = {} 

for i in range(N): 
    for j in range(len(alpha[i])): 
        if alpha[i][j] in alpha_dict: 
            alpha_dict[alpha[i][j]] += 10 ** (len(alpha[i])-j-1) 
        else:   
            alpha_dict[alpha[i][j]] = 10 ** (len(alpha[i])-j-1)

numList = sorted(alpha_dict.values(),reverse=True)
total = 0
num = 9
for i in numList: 
    total += num * i
    num -= 1

print(total)
