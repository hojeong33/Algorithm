#이항계수1
N,K=map(int,input().split())
n=1
k=1
for i in range(N,N-K,-1):
    n*=i
for i in range(1,K+1):
    k*=i
print(n//k)
