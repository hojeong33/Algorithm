a,b=input().split()
new_a=''
new_b=''
for i in range(len(a)-1,-1,-1):
    new_a+=a[i]
for i in range(len(b)-1,-1,-1):
    new_b+=b[i]
if int(new_a)>int(new_b):
    print(new_a)
else:
    print(new_b)
