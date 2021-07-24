cnt=int(input())
ans_list=[]
for i in range(cnt):
    right_list=input()
    score=[]
    right_cnt=0
    for j in right_list:
        if j=='O':
            right_cnt+=1
        else:
            right_cnt=0
        score.append(right_cnt)
    ans_list.append(sum(score))
for i in range(cnt):
    print(ans_list[i])