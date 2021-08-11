#달팽이는 올라가고 싶다
A, B, V=map(int,input().split())
cnt=(V-A)//(A-B)
h=(A-B)*cnt
while h<V:
   if h+A>=V:
       cnt+=1
       break
   elif h+A-B<0:
       h=0
   else:
       h=h+A-B
   cnt+=1
print(cnt)