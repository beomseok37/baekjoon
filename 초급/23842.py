N = int(input())

number = [6,2,5,5,4,5,6,3,7,6]

for i1 in range(10):
  for i2 in range(10):
    for i3 in range(10):
      for i4 in range(10):
        for i5 in range(10):
          for i6 in range(10):
            if number[i1]+number[i2]+number[i3]+number[i4]+number[i5]+number[i6] != N-4:
              continue
            if i1*10+i2+i3*10+i4==i5*10+i6:
              print(str(i1)+str(i2)+"+"+str(i3)+str(i4)+"="+str(i5)+str(i6))
              exit()

print('impossible')
