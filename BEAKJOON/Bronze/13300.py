# 방 배정
N,K=map(int,input().split())
m=[]
w=[]
for i in range(N):
    s,g=map(int,input().split())
    if s==1:
        m.append(g)
    else:
        w.append(g)
l_m=len(set(m))
l_w=len(set(w))

for i in list(set(w)):
    c=w.count(i)
    if c>K:
        if c%K==0:
            temp=c//K
        else:
            temp=c//K+1
        l_w+=temp-1

for i in list(set(m)):
    c = m.count(i)
    if c>K:
        if c%K==0:
            temp=c//K
        else:
            temp=c//K+1
        l_m+=temp-1
print(l_w+l_m)
