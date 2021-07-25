N = input()
ans=0
max_sum=(len(N)-1)*9+(int(N[0])-1)
for i in range(max_sum,0,-1):
    my_num=int(N)-i
    my_sum=my_num
    for j in str(my_num):
        my_sum+=int(j)
    if my_sum==int(N):
        ans=my_num
        break
print(ans)
