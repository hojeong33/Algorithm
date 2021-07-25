num=int(input())
cnt=1
ans=0
sum=1
if num==1:
    ans=1
else:
    for i in range(num):
        sum+=i*6
        if sum <num:
            cnt+=1
        else:
            break
print(cnt)