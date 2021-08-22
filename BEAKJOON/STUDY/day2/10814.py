#나이순 정렬
N=int(input())
name=[]
age=[]
for i in range(N):
    a,n=input().split()
    name.append(n)
    age.append(int(a))
while age:
    for i in range(len(age)):
        num=age[0]
        num_index=0
        if num>age[i]:
            num=age[i]
            num_index=i
    print('{} {}'.format(age[num_index],name[num_index]))
    age.pop(num_index)
    name.pop(num_index)

