t = int(input())
for _ in range(t):
    num = list(map(int, input().split()))
    min_even_num = 101
    total = 0
    for n in num:
        if n % 2 == 0:
            total += n
            min_even_num = min(n, min_even_num)
    print(total, min_even_num)
