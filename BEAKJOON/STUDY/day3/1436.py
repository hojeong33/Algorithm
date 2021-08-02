start,end=map(int,(input().split()))
n_list=[]
flag=False
for i in range(end):
    for j in range(i):
        n_list.append(i)
        if len(n_list)==end:
            flag=True
            break
    if flag:
        break

     
n_list=n_list[start-1:]

print(sum(n_list))