#컵홀더
N=int(input())
seat=input()
cnt_s=0
cnt_l=0
for i in seat:
    if i=='S':
        cnt_s+=1
    else:
        cnt_l+=1
cnt_l=cnt_l//2
if cnt_l>0:
    print(cnt_s+cnt_l+1)
else:
    print(cnt_s)

