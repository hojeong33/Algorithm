ans=[]
while 1:
    num=int(input())
    if num==0:
        break
    else:
        str_num=''
        num=str(num)
        for i in range(len(num)-1,-1,-1):
            str_num+=num[i]
        if num==str_num:
            ans.append('yes')
        else:
            ans.append('no')
        num=int(num)
print(*ans,sep='\n')
        
