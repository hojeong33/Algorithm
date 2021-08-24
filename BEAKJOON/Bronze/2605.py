# 줄 세우기
N=int(input())
p=list(map(int,input().split()))
ans=[0]*N
for i in range(N):
    if p[i]:
        k=i-p[i]
        back=i-1
        cnt=0
        while cnt<=p[i]:
            temp=ans[back]
            ans[back+1]=temp
            cnt+=1
            back-=1
        ans[k]=i+1
    else:
        ans[i]=i+1
print(*ans)
