num = int(input())
cnt = 0
for i in range(1, int(num**0.5) + 1):
    if num % i == 0:
        cnt += 1 if num // i == i else 2
print(cnt)
