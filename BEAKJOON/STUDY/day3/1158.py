#요세푸스 문제
N,K=map(int,input().split()) #N명의 사람, K번째 사람 제거
pre_list=[] # 1~N까지의 사람을 리스트로 
del_list=[] #제거 된 사람들을 정렬

# 1~N번까지 사람 정렬
for i in range(1,N+1):
    pre_list.append(i)
# 사람 모두를 제거해야하니 N번 순회
for i in range(N):
    if K<=len(pre_list): # 현재 사람 수가 k번째 보다 큰 경우
        del_list.append(pre_list.pop(K-1)) #해당 인덱스를 제거하고 바로 델리스트에 추가함
        pre_list=pre_list[K-1:]+pre_list[:K-1] #제거된 인덱스 기준으로 앞에있는 사람들을 뒤로 보냄
    else: #현재 사람 수가 k번째 보다 작은  경우 121212??
        K2=K%(len(pre_list)) #k2번째 사람 제거
        if K2==0: #나누어 떨어질 때는 길이를 k2
            K2=len(pre_list)
        del_list.append(pre_list.pop(K2-1))#인덱스 접근을 위해서 -1
        pre_list=pre_list[K2-1:]+pre_list[:K2-1]

#출력 형식 맞추기 <1, 2, 3, 4..>        
print('<',end='')
print(', '.join(repr(e)for e in del_list),end='>')