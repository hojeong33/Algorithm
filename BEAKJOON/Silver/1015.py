# 수열 정렬
N = int(input())
A = list(map(int, input().split()))
B = sorted(A)
ans=[]
for i in A:
    temp=B.index(i)
    while 1:
        if temp in ans:
            temp+=1
        else:
            break
    ans.append(temp)
print(*ans)
