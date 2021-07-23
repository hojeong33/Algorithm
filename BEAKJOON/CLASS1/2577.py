num1=int(input())
num2=int(input())
num3=int(input())
total=str(num1*num2*num3)
for i in range(10):
    cnt=0
    for j in range(len(total)):
        if str(i)==total[j]:
            cnt+=1
    print(cnt)


