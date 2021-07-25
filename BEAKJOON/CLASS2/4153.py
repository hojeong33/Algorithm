ans_list=[]
while True:
    num1,num2,num3=map(int,input().split())
    if num1+num2+num3==0:
        break
    else:
        num_list=[num1,num2,num3]
        max_num=max(num_list)
        num_list.remove(max_num)
        total=0
        for i in num_list:
            total+=i**2
        if max_num**2==total:
            ans_list.append('right')
        else:
            ans_list.append('wrong')
for i in ans_list:
    print(i)
