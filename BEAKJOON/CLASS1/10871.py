a,b= input().split()
lst=input().split()
lst=list(lst)
ans=[]
for i in lst:
    if int(b)>int(i):
        ans.append(int(i))
print(*ans)