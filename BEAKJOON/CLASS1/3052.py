ans_set=[]
for i in range(10):
    num=int(input())
    ans_set.append(num%42)
ans_set=set(ans_set)
print(len(ans_set))