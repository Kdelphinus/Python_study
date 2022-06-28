n = int(input())
star, blank = "*", " "
for i in range(n, 0, -1):
    print(f"{blank * (n - i)}{star * (i * 2 - 1)}")
for i in range(2, n + 1):
    print(f"{blank * (n - i)}{star * (i * 2 - 1)}")
