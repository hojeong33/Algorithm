#설탕배달
kg=int(input())
max_cnt=kg
flag=False
for i in range(0,max_cnt+1):
    for j in range(0,max_cnt+1):
        if i*3+j*5==kg:
            ans=i+j
            flag=True
            break
        else:
            ans=-1       
    if(flag):
        break
print(ans)