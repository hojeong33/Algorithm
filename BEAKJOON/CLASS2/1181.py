#단어 정렬
cnt=int(input())
words=[]
for i in range(cnt):
    words.append(input())
words=list(set(words))
for i in range(len(words)):
    for j in range(i,len(words)):
        if len(words[i])>len(words[j]):
            temp=words[i]
            words[i]=words[j]
            words[j]=temp
        elif len(words[i])==len(words[j]):
            if words[i]>words[j]:
                temp=words[i]
                words[i]=words[j]
                words[j]=temp
print(*words,sep='\n') 
                
