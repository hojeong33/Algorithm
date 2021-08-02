#쉽게 푸는 문제
start,end=map(int,(input().split()))
n_list=[]
for i in range(1,46): # range(1,end)까지로 하면?
    n_list+=[i]*i
print(sum(n_list[start-1:end]))