#요세푸스 문제
N,K=map(int,input().split())
pre_list=[]
del_list=[]
for i in range(1,N+1):
    pre_list.append(i)
for i in range(N):
    if K<=len(pre_list):
        del_list.append(pre_list.pop(K-1))
        pre_list=pre_list[K-1:]+pre_list[:K-1]
    else:
        K2=K%(len(pre_list))
        if K2==0:
            K2=len(pre_list)
        del_list.append(pre_list.pop(K2-1))
        pre_list=pre_list[K2-1:]+pre_list[:K2-1]
print('<',end='')
print(', '.join(repr(e)for e in del_list),end='>')