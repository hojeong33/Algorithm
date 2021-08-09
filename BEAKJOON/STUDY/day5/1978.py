def isPrime(a):
    cnt=0
    for i in range(1,a+1):
        if a%i==0:
            cnt+=1
    if cnt==2:
        return 1
    else:
        return 0

N=int(input())
n_list=list(map(int,input().split()))
total=0
for i in n_list:
    total+=isPrime(i)
print(total)