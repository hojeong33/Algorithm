#약수
n=int(input()) # 진짜 약수 개수 
n_lst=list(map(int,input().split())) # 진짜 약수 인트로 받고 리스트로 묶음
n_lst.sort() #리스트를 정렬함 
print(n_lst[0]*n_lst[-1]) #첫값과 끝값의 곱이 N
