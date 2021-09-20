# 팩토리얼 0의 개수
N=int(input())
num=1
for i in range(1,N+1):
    num*=i
num=str(num)
ans=0
for i in range(len(num)-1,-1,-1):
    if num[i]=='0':
        ans+=1
    else:
        print(ans)
        break
