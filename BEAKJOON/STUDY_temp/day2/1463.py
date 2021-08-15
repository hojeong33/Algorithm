#1로 만들기
n=int(input())
f_list=[n]
cnt=0
if n==1:
    print(0)
else:
    while 1:
        cnt+=1
        n_list=[]
        for i in f_list:
            if i%3==0:
                n_list.append(i//3)
            if i%2==0:
                n_list.append(i//2)
            n_list.append(i-1)
        if 1 in n_list:
            break
        f_list=list(set(n_list))
        
print(cnt)