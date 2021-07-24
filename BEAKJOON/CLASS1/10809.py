ans_list=[]
ans=0
word=input()
for i in range(97,123):
    for j in range(len(word)):
        if i==ord(word[j]):
            ans=j
            break
        else:
            ans=-1
    ans_list.append(ans)
for i in range(len(ans_list)):
    print(ans_list[i],end=' ')