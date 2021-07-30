#1로 만들기
n=int(input())
cnt=0
while n !=1:
    if (n-1)%3==0 and (n//2)%2:
        n-=1
    elif n%3==0:
        n//=3
    elif n%2==0:
        n//=2
    else:
        n-=1
    cnt+=1
print(cnt)
