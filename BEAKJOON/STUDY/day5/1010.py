#다리 놓기
T=int(input())

for tc in range(T):
    
    N,M=map(int,input().split())
    cnt=1
    num=1
    # M개 중에 N개 뽑기
    for i in range(M,M-N,-1):
        cnt*=i
    # 중복되는 경우 나눠주기
    for i in range(N,0,-1):
        num*=i
    cnt//=num
    print(cnt)



