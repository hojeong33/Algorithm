#이차원 배열과 연산
a=[[1,2],[2,3],[2,1],[1,3]]
a.sort()
print(a)
a.sort(key=lambda x:x[1])
print(a)
a.sort(key=lambda x:x[0])
print(a)
a.sort(key=lambda x:(x[1],x[0]))
print(a)
