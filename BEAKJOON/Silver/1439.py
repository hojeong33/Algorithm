#뒤집기
def all_change():
    for i in S:
        if i==0:
            i=1
        else:
            i=0

S=list(map(int,input()))
n=len(S)
ans=0
while 1:
    cnt=0
    for i in range(n-1):
        if S[i]!=S[i+1]:
            cnt+=1
    cnt-=1
    if cnt==0:
        print(ans)
        break
    elif cnt==1:
        ans+=1
        print(ans)
        break
    else:
        all_change()
        ans+=1



