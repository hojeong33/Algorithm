name="JEROEN"
check=[False]*len(name)
check_num=0
for i in range(len(name)):
    if name[i]=='A':
        check[i]=True
        check_num+=1
idx=0
cnt=0
d=1
while 1:
    if check[idx]==False:
        temp=abs(ord('A')-ord(name[idx]))
        cnt+=min(temp,26-temp)
        check[idx]=True
        check_num+=1
    if check_num==len(name):
        break
    if check[idx+d]:
        d*=-1
    idx+=d
    print(idx)
    cnt+=1
print(cnt)