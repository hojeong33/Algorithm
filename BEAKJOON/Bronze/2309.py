#일곱난쟁이
p=[int(input()) for _ in range(9)]
s=sum(p)-100
flag=False
for i in range(8):
    for j in range(i+1,9):
        if p[i]+p[j]==s:
            if i<j:
                p.pop(j)
                p.pop(i)
            else:
                p.pop(i)
                p.pop(j)
            flag=True
            break
    if flag:
        break
p.sort()
for i in p:
    print(i)