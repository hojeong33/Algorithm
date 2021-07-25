cnt=int(input())
ans_list=[]
for i in range(cnt):
    h,w,n=map(int,input().split())
    ans=''
    if n%h==0:
        ans+=str(h)
        if (n//h)<10:
            ans+='0'+str((n//h))
        else:
            ans+=str((n//h))
    else:
        ans+=str(n%h)
        if (n//h)+1<10:
            ans+='0'+str((n//h)+1)
        else:
            ans+=str((n//h)+1)
    ans_list.append(ans)
for i in ans_list:
    print(i)