# 2 X 타일링 2
t = [0, 1, 3]
for i in range(3, 1001):
    t.append(t[i - 2] * 2 + t[i - 1])
n = int(input())
print(t[n] % 10007)
