# 영역 구하기
import sys
sys.setrecursionlimit(10**9)

dr=[-1,1,0,0]
dc=[0,0,-1,1]

def dfs(r,c):
    global temp
    arr[r][c]=3
    for d in range(4):
        nr=r+dr[d]
        nc=c+dc[d]
        if 0<=nr<M and 0<=nc<N and not arr[nr][nc]:
            arr[r][c]=3
            dfs(nr,nc)
            temp+=1




M,N,K=map(int,input().split()) # M: 행, N: 열, K:직사각형 개수
l_b=[[] for _ in range(K)]
r_u=[[] for _ in range(K)]
arr=[[0]*N for _ in range(M)]

for i in range(K):
    l_c,l_r,r_c,r_r=map(int,input().split())
    l_b[i].append(M-1-l_r)
    l_b[i].append(l_c)
    r_u[i].append(M-r_r)
    r_u[i].append(r_c-1)
for i in range(K):
    for r in range(r_u[i][0],l_b[i][0]+1):
        for c in range(l_b[i][1],r_u[i][1]+1):
            arr[r][c]=1
ans=[]
for r in range(M):
    for c in range(N):
        if not arr[r][c]:
            temp=1
            dfs(r,c)
            ans.append(temp)
ans.sort()
print(len(ans))
print(*ans)

