X,Y,D,T=list(map(int,input().split()))

d=(X**2+Y**2)**(1/2)
share=d//D
remain=d%D
minValue = min(d,share * T + remain,(share+1)*T + D-remain)

if d%D==0:
    minValue=min(minValue,share*T)
else:
    if share<=1:
        minValue=min(minValue,2*T)
    else:
        minValue=min(minValue,(share+1)*T)

print(minValue)
