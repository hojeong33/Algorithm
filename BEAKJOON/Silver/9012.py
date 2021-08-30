#괄호
T=int(input())
for tc in range(T):
    s=list(input())
    cnt=0
    ans='YES'
    for i in s:
        if i=='(':
            cnt+=1
        else:
            cnt-=1
        if cnt<0:
            ans='NO'
            break
    else:
        if cnt!=0:
            ans='NO'
    print(ans)


