# 덩치
N=int(input())
key=[]
weight=[]
for i in range(N):
        w,k=map(int,input().split())
        weight.append(w)
        key.append(k)
for i in range(N):
    cnt=1
    for j in range(N):
        if key[i] < key[j] and weight[i] < weight[j]:
            cnt+=1
    print(cnt)