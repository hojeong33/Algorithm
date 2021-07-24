num_list=input().split()
ans=''
if num_list[0]=='1':
    for i in range(1,9):
        if str(i) == num_list[i-1]:
            ans='ascending'
        else:
            ans='mixed'
elif num_list[0]=='8':
    for i in range(8,0,-1):
        if str(i)==num_list[8-i]:
            ans='descending'
        else:
            ans='mixed'
else:
    ans='mixed'
print(ans)     