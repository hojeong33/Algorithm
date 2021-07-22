number=input()
for i in range(1,int(number)+1):
    k=int(number)-i
    print(' '*k,end='')
    print('*'*i)
