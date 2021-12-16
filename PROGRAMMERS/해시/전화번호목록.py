phone_book=["119", "97674223", "1195524421"]
answer=True
for i in range(len(phone_book)-1):
    l_1=len(phone_book[i])
    for j in range(i+1,len(phone_book)):
      l_2=len(phone_book[j])
      if l_1<l_2 and  phone_book[i]==phone_book[j][:l_1]:
          answer=False
      elif phone_book[i][:l_2]==phone_book[j]:
          answer=False
    if not answer:
        break
print(answer)