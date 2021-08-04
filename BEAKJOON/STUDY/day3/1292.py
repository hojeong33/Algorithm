#쉽게 푸는 문제
start,end=map(int,(input().split()))
n_list=[]
for i in range(1,46): # range(1,end)까지로 하면?
    n_list+=[i]*i
print(sum(n_list[start-1:end]))


# 입력값 제어??
# cnt=0
# flag=False
# while 1:
#     for i in range(1,1000):
#         for j in range(i):
#             cnt+=1
#             if cnt==1000:
#                 print(i)
#                 flag=True
#                 break
#     if flag:
#         break


        

    