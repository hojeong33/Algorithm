def solution(phone_book):
    answer=True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        l_1=len(phone_book[i])
        l_2=len(phone_book[i+1])
        if l_1<l_2 and  phone_book[i]==phone_book[i+1][:l_1]:
            answer=False
        elif phone_book[i][:l_2]==phone_book[i+1]:
            answer=False
        if not answer:
            break
    return answer