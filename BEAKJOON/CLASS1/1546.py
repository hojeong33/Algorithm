cnt=int(input())
scores=input().split()
n_scores=[]
sum_scores=0
for i in scores:
    n_scores.append(int(i))
max_score=max(n_scores)
for i in n_scores:
    sum_scores+=i/max_score*100
print(sum_scores/cnt)
