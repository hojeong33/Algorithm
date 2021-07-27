#신기한 네자리 숫자
ans_list=[]
def sum_num(num1,num2):
    total=0
    while num1>0:
        total+=num1%num2
        num1//=num2
    return total

for i in range(1000,10000):
    if sum_num(i,10)==sum_num(i,12)==sum_num(i,16):
        ans_list.append(i)

for i in ans_list:
    print(i)