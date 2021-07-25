def people_count(m_k,m_n):
    if m_k==0:
        return m_n
    elif m_k==1:
        m_sum=0
        for i in range(m_n+1):
            m_sum+=people_count(0,i)
        return m_sum
    else:
        return people_count(m_k,m_n-1) + people_count(m_k-1,m_n)

ans=[]
cnt=int(input())
for i in range(cnt):
    k=int(input())
    n=int(input())
    ans.append(people_count(k,n))
for i in range(cnt):
    print(ans[i])
