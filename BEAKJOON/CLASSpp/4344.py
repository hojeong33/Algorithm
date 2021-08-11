#평균은 넘겠지
C=int(input())
for tc in range(C):
    n_list=list(map(int,input().split()))
    total=0
    for i in n_list[1:]:
        total+=i
    avg=total/n_list[0]
    cnt=0
    for i in n_list[1:]:
        if i>avg:
            cnt+=1
    print('{:.3f}%'.format((cnt/n_list[0])*100))