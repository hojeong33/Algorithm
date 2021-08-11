#셀프 넘버
numbers=set(range(1,10000))
remove_set=set()
for num in numbers:
    for n in str(num):
        num+=int(n)
    remove_set.add(num)

my_numbers=numbers-remove_set

print(*sorted(my_numbers),sep='\n')