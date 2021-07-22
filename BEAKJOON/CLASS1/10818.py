cnt=int(input())
numbers=input().split()
numbers=list(numbers)
my_max=int(numbers[0])
my_min=int(numbers[0])
for i in numbers:
    if int(i) > my_max:
        my_max=int(i)
    if int(i)<my_min:
        my_min=int(i)
print(my_min, my_max)
