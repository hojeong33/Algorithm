#블랙잭
n,m=map(int,input().split())
num_list=list(map(int,input().split()))
max_sum=0
for i in range(n-1,0,-1):
    for j in range(n-2,0,-1):
        for k in range(n-3,0,-1):
            if num_list[i] !=num_list[j]!=num_list[k]!=num_list[i]:
                if max_sum < num_list[i]+num_list[j]+num_list[k]<=m:
                    max_sum=num_list[i]+num_list[j]+num_list[k]
print(max_sum)
    