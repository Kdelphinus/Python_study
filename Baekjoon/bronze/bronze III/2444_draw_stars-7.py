n = int(input())
star, blank = "*", " "
for i in range(1, n + 1):
    print(blank * (n - i), end="")
    print(star * (2 * i - 1))
for i in range(n - 1, 0, -1):
    print(blank * (n - i), end="")
    print(star * (2 * i - 1))
