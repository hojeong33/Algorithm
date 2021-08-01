#체스판 다시 칠하기
#BBWBWBW...첫문자를 바꾸는 것이 가장 적을 수도 있으니 IF 문으로 분리하지 않는다.
M,N=map(int,input().split())
m_n=[]
for i in range(M):
    m_n.append(list(input()))
cnt=0
cnt_list=[]
for m in range(M-7):
    for n in range(N-7):
        for i in range(m,m+8,2):
            for j in range(n,n+8,2):
                if m_n[i][j]=='W':
                    pass
                else:
                    cnt+=1
            for j in range(n+1,n+8,2):
                if m_n[i][j]=='B':
                    pass
                else:
                    cnt+=1
        for i in range(m+1,m+8,2):
            for j in range(n,n+8,2):
                if m_n[i][j]=='B':
                    pass
                else:
                    cnt+=1
            for j in range(n+1,n+8,2):
                if m_n[i][j]=='W':
                    pass
                else:
                    cnt+=1
        cnt_list.append(cnt)
        cnt=0
        for i in range(m,m+8,2):
            for j in range(n,n+8,2):
                if m_n[i][j]=='B':
                    pass
                else:
                    cnt+=1
            for j in range(n+1,n+8,2):
                if m_n[i][j]=='W':
                    pass
                else:
                    cnt+=1
        for i in range(m+1,m+8,2):
            for j in range(n,n+8,2):
                if m_n[i][j]=='W':
                    pass
                else:
                    cnt+=1
            for j in range(n+1,n+8,2):
                if m_n[i][j]=='B':
                    pass
                else:
                    cnt+=1
        cnt_list.append(cnt)
        cnt=0
        
print(min(cnt_list))
        