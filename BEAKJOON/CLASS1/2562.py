lst=[]
ans_num=0
ans_cnt=0
cnt=0
for i in range(9):
        a=int(input())
        lst.append(a)
        cnt+=1
        if a==max(lst):
            ans_num=a
            ans_cnt=cnt
print(ans_num)
print(ans_cnt)