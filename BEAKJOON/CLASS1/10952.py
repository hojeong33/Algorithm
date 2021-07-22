a,b=input().split()
lst=[]
while a!='0' and b!='0':
    lst.append(int(a)+int(b))
    a,b=input().split()
for i in lst:
    print(i)