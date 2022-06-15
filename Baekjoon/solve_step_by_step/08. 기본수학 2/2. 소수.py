""" 2581 소수 """
m = int(input())
n = int(input())
num = []

for i in range(m, n + 1):
    cnt = 0
    if i == 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            cnt += 1
            break
    if cnt == 0:
        num.append(i)

if 1 <= len(num):
    print(sum(num))
    print(min(num))
else:
    print(-1)
