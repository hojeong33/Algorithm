# 수 정렬하기2
def myMax(*args):
    num=args[0]
    for i in args:
        if num<i:
            num=i
    return num

N = int(input())
n_list = [int(input()) for _ in range(N)]
counting = [0] * (myMax(*n_list) + 1)*2

for i in n_list:
    if i<0:
        counting[-i] += 1
    else:
        counting[i]+=1
for i in range(len(counting)):
    if counting[i]:
        print(i)

# 버블정렬
# for i in range(len(n_list)-1,0,-1):
#     for j in range(1,i+1):
#         if n_list[j]<n_list[j-1]:
#             n_list[j],n_list[j-1]=n_list[j-1],n_list[j]
# print(*n_list,sep='\n')
