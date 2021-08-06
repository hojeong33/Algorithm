#숫자 정사각형
N,M=map(int,input().split())
m_list=[]
for i in range(N):
    m_list.append(list(map(int,input())))
max=min(N,M)
cnt=0
for i in range(N):
    for j in range(M):
        for m in range(max):
            if i+m<N and j+m<M:
                if m_list[i][j]==m_list[i+m][j]==m_list[i][j+m]==m_list[i+m][j+m]:
                    if cnt<m:
                        cnt=m 
print((cnt+1)**2)