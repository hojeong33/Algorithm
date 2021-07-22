my_word=input()
my_word=my_word.upper()
cnt=0
ans=''
for i in range(len(my_word)):
    if cnt<my_word.count(my_word[i]):
        cnt=my_word.count(my_word[i])
        ans=my_word[i]
    elif cnt==my_word.count(my_word[i]) and ans!=my_word[i]:
        ans='?'
print(ans)        
