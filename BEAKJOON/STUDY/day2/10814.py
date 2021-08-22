#나이순 정렬
import operator
N=int(input())
my_dic={}
for i in range(N):
    a,n=input().split()
    my_dic[n]=int(a)
result=sorted(my_dic.items(),key=lambda x:x[1]) # key=operator.itemgetter(1)
for i in range(N):
    print('{} {}'.format(result[i][1],result[i][0]))

# def mySort(lst):
#     for i in range(len(lst)-1,0,-1):
#         for j in range(0,i):
#             if lst[j][0]>lst[j+1][0]:
#                 lst[j],lst[j+1]=lst[j+1],lst[j]
#     return lst
# def selectionSort(lst):
#     for i in range(len(lst)-1):
#         min=i
#         for j in range(i+1,len(lst)):
#             if lst[min][0]>=lst[j][0]:
#                 min=j
#         lst[i],lst[min]=lst[min],lst[i]
#     return lst


