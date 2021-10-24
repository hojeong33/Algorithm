def people_count(m_k,m_n):
    if m_k==0:
        people=m_n
    elif m_n==1:
        people=1
    else:
        people=people_count(m_k,m_n-1)+people_count(m_k-1,m_n)
    return people
    


ans=[]
cnt=int(input())
for i in range(cnt):
    k=int(input())
    n=int(input())
    ans.append(people_count(k,n))

print(*ans,sep='\n')

