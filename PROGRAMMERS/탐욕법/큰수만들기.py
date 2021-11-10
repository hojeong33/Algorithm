from itertools import combinations
def solution(number, k):
    combination=combinations(range(len(number)),k)
    temps=[]
    for i in combination:
        temp=list(number)
        for j in range(k-1,-1,-1):
            temp.pop(i[j])
        num=''
        for j in temp:
            num+=j
        temps.append(num)
    return max(temps)