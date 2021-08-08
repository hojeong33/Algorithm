#최대공약수와 최소공배수
n1,n2=map(int,input().split())
def max_n(n1,n2):
    while n2>0:
        n1,n2=n2,n1%n2
    return n1
def min_n(n1,n2):
    return n1*n2//max_n(n1,n2)
print(max_n(n1,n2))
print(min_n(n1,n2))

#math 모듈 사용하기
# import math
# n1,n2=map(int,input().split())
# print(math.gcd(n1,n2))
# print(math.lcm(n1,n2))

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

# n1,n2=map(int,input().split())
# n1_list=[]
# n2_list=[]

# for i in range(1,n1):
#     if n1%i==0:
#         n1_list.append(i)
# for i in range(1,n2):
#     if n2%i==0:
#         n2_list.append(i)
# a=set(n1_list)&set(n2_list)
# print(max(a))
# print(n1*n2//max(a))





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

