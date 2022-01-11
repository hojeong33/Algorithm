#미세먼지안녕
from copy import deepcopy
# 입력
R,C,T=map(int,input().split()) # R:행, C:열, T:초
room=[[]for _ in range(R)]
for i in range(R):
    room[i]=list(map(int,input().split()))

m=[]
for i in range(R):
    for j in range(C):
        if room[i][j]==-1:
            m.append(i)

#확산

dr=[0,-1,0,1]
dc=[1,0,-1,0]

def bfs(r,c):
    check = [[0] * C for _ in range(R)]
    cnt=0
    A = room[r][c]
    a = A // 5
    for d in range(4):
        nr=r+dr[d]
        nc=c+dc[d]
        if nr<0 or nr>=R or nc<0 or nc>=C:
            continue
        if room[nr][nc]==-1:
            continue
        cnt+=1
        check[nr][nc]+=a
    room[r][c]-=cnt*a

    for i in range(R):
        for j in range(C):
            room[i][j] += check[i][j]

while T:
    for i in range(R):
        for j in range(C):
            if room[i][j]>=5:
                bfs(i,j)


    # 공기청정기 작동
    tmp=deepcopy(room)
    m1=m[0]
    m2=m[1]
    for c in range(2,C-1):
        tmp[m1][c]=room[m1][c-1]
        tmp[0][c]=room[0][c+1]
        tmp[m2][c]=room[m2][c-1]
        tmp[R-1][c]=room[R-1][c+1]
    for r in range(0,m1):
        tmp[r][C-1]=room[r+1][C-1]
        tmp[r][0]=room[r-1][0]
    for r in range(m2+1,R-1):
        tmp[r][C-1]=room[r-1][C-1]
        tmp[r][0]=room[r+1][0]

    tmp[m1][1]=0
    tmp[m2][1]=0

    tmp[m1][C-1]=room[m1][C-2]
    tmp[m2][C-1]=room[m2][C-2]

    tmp[0][C-1]=room[1][C-1]
    tmp[0][1]=room[0][2]
    tmp[0][0]=room[0][1]

    tmp[R-1][C-1]=room[R-2][C-1]
    tmp[R-1][1]=room[R-1][2]
    tmp[R-1][0]=room[R-1][1]

    room=deepcopy(tmp)
    T-=1
ans=0
for i in range(R):
    for j in range(C):
        if tmp[i][j]!=-1:
            ans+=tmp[i][j]
print(ans)