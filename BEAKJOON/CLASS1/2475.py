number=input().split()
total=0
for i in list(number):
    total+=int(i)**2
print(total%10)