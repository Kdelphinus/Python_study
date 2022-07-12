min_number = 101
total = 0
for _ in range(7):
    n = int(input())
    if n % 2:
        total += n
        min_number = min(n, min_number)
if total:
    print(total)
    print(min_number)
else:
    print(-1)
