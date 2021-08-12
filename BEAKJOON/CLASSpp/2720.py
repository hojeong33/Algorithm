#세탁소 사장 동혁
# Q=25 D=10 N=5 P=1  --> Q만 배수 관계 성립이 안된다!
T=int(input())
for tc in range(T):
    C=int(input())
    Q=C//25
    q=C%25
    D=q//10
    d=q%10
    N=d//5
    n=d%5
    P=n//1
    print('{} {} {} {}'.format(Q,D,N,P))
