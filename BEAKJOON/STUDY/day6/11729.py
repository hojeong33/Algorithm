# 하노이 탑 이동 순서
def hanoi(n,a,b,c):
    if n==0:
        return
    else:
        hanoi(n-1,a,c,b)
        print(a,c)
        hanoi(n-1,b,a,c)

n=int(input())
sum=1
for i in range(n-1):
    sum=sum*2+1
print(sum)
hanoi(n,1,2,3)