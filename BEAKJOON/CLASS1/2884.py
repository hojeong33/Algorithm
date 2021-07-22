h,m=input().split()
h=int(h)
m=int(m)
if m>=45:
    m-=45
else:
    m+=15
    if h==0:
        h=23
    else:
        h-=1
print(h, m)