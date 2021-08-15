# 만취한 상범
cnt= int(input())
escape=[]
ans=[]
for i in range(cnt):
    num=int(input())
    ans=[0]*num
    for my_round in range(1,num+1):
        for room in range(1,len(ans)+1):
            if room%my_round==0:
                if ans[room-1]==0:
                    ans[room-1]=1
                elif ans[room-1]==1:
                    ans[room-1]=0
    escape.append(ans.count(1))
for i in escape:
    print(i)
    