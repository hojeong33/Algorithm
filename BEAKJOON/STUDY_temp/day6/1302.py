#베스트셀러
N=int(input())
book={}
for i in range(N):
    name=input()
    if not name in book.keys():
        book[name]=1
    else:
        book[name]+=1



