#최대공약수와 최소공배수
#시간초과 

# n1,n2=map(int,input().split())

# j=min(n1,n2)
# while 1:
#     if n1%j==0 and n2%j==0:
#         print(j)
#         break
#     else:
#         j-=1

# k=max(n1,n2)
# while 1:
#     if k%n1==0 and k%n2==0:
#         print(k)
#         break
#     else:
#         k+=1

#시간초과

n1,n2=map(int,input().split())
n1_list=[]
n2_list=[]

for i in range(1,n1):
    if n1%i==0:
        n1_list.append(i)
for i in range(1,n2):
    if n2%i==0:
        n2_list.append(i)
a=set(n1_list)&set(n2_list)
b=set(n1_list)^set(n2_list)
print(a)
print(b)





#시간초과
# n1,n2=map(int,input().split())
# max_num=1 #최대공약수
# min_num=n1*n2 #최소공배수
# for i in range(1,min(n1,n2)+1):
#     if n1%i==0 and n2%i==0:
#         if max_num<i:
#             max_num=i
# for i in range(n1*n2,min(n1,n2),-1):
#     if i%n1==0 and i%n2==0:
#         if min_num>i:
#             min_num=i   
# print(max_num)
# print(min_num)

