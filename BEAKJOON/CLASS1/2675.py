cnt= int(input())
ans_list=[]
ans_str=''
for i in range(cnt):
    a,b=input().split()
    for j in b:
        ans_str+=j*int(a)
    ans_list.append(ans_str)
    ans_str=''
for k in ans_list:
    print(k)

