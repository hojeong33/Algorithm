my_word=list(input().upper())
ans_list=[]
for i in range(65,91):
    cnt=0
    for j in my_word:
        if chr(i)==j:
            cnt+=1
    ans_list.append(cnt)
my_max=max(ans_list)
my_count=ans_list.count(my_max)
if my_count==1:
    for k in range(26):
        if ans_list[k]==my_max:
            print(chr(k+65))
else:
    print('?')      
