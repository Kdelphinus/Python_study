a, b = map(int, input().split())
num = [0]
for i in range(1, b + 1):
    for _ in range(i):
        num.append(num[-1] + i)
print(num[b] - num[a - 1])
