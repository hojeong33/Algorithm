# 이친수
N=int(input())
ans=0
lst=[0 for _ in range(N)]
lst[0]=1
cnt=2**(N-1)
for i in range(cnt):
    