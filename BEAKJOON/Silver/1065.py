# 한수
N=int(input())
ans=0
cnt=0

for i in range(1,N+1):
    if i<=99:
        cnt+=1
    elif i==1000:
        continue
    else:
        s=str(i)
        s1=int(s[0])-int(s[1])
        s2=int(s[1])-int(s[2])
        if s1==s2:
            cnt+=1
print(cnt)